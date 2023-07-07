import pandas as pd
from .filter.abstractFilter import abstractFilter
from .cleaner.abstractCleaner import abstractCleaner
from datetime import timedelta
import logging

logger = logging.getLogger('cartobat')

class Preprocessor:
    """
    Preprocessor class, used to preprocess the data
    set you're cleaner and filter (with set_cleaner and set_filter),
    before calling process()
    args:
        rssi_df: dataframe containing the data to preprocess
        sampling_time: time between each sample, if None, base sampling is 0.5 seconds
    
    
    """
    def __init__(self,rssi_df,*, sampling_time=None) -> None:
        self.rssi_df=rssi_df
        self.filter=None
        self.cleaner=None
        self.sampling_time= timedelta(seconds=sampling_time) if sampling_time!=None else timedelta(seconds=0.5)#0.5 seconds window by default

    def sampling(self,rssi_df):
        #data must be sorted by timestamp
        sampling_time=self.sampling_time
        min_time=min(rssi_df['timestamp']).round(freq='500L')-sampling_time#round th inferior
        max_time=max(rssi_df['timestamp']).round(freq='500L')+sampling_time#round to superior
        time_range=pd.date_range(min_time,max_time,freq=sampling_time)
        count=0
        sampled_df=pd.DataFrame(columns=rssi_df.columns)
        mac_module=rssi_df['macModule'].iloc[0]
        logger.info(f'{rssi_df=}')

        for i in time_range:
            #logger.info(f'i: {i}')
            signal_intensity=-100#certainly not the best way to do it
            while count< len(rssi_df) and i>rssi_df['timestamp'].iloc[count]:
                signal_intensity=max(rssi_df['rssi'].iloc[count],signal_intensity)
                #logger.debug('count: '+str(count)+' signal_intensity:'+str(signal_intensity))

                count+=1
            sampled_df=self._add_row(sampled_df,pd.DataFrame({'timestamp':i,'rssi':signal_intensity,'macModule':mac_module},index=[0]))
        return sampled_df
    def set_cleaner(self,cleaner)->'Preprocessor':
        self.cleaner=cleaner
        return self
    def set_filter(self,filter:abstractFilter)->'Preprocessor':
        self.filter=filter
        return self
    @staticmethod
    def _add_row(df, row):
        df=pd.concat([df,row],ignore_index=True)
        return df
    def __segmenting(self,rssi_df):
        #must clean this : use add_row

        mac_module_list=rssi_df['macModule'].unique()
        empty_df = pd.DataFrame(columns=rssi_df.columns)
        filtered_df=empty_df.copy()
        for mac_module in mac_module_list:
            
            mac_module_rssi=rssi_df[rssi_df['macModule']==mac_module]
            segment=empty_df.copy()
            previous_time=mac_module_rssi.iloc[0]['timestamp']
            for index,row in mac_module_rssi.iterrows():
                row=row.transpose()
                delay=row['timestamp']-previous_time
                if (delay>100*self.sampling_time):
                    filtered_df=pd.concat([filtered_df,self.filter(segment)])#type: ignore
                    segment=empty_df.copy()
                else:
                    test=pd.DataFrame(row).transpose()
                    segment=pd.concat([segment,test],ignore_index=True)#type: ignore

                previous_time=row['timestamp']

            if not segment.empty : filtered_df=pd.concat([filtered_df,self.filter(segment)],ignore_index=True)

        #sort by timestamp the filtered_df
        filtered_df=filtered_df.sort_values('timestamp',ascending=True ) # type: ignore
        return(filtered_df)
    def process(self)->'pd.DataFrame':
        if not issubclass(type(self.cleaner), abstractCleaner):
            raise TypeError("Cleaner is not set, please use set_cleaner(cleaner:function)")
        if not issubclass(type(self.filter), abstractFilter):
            raise TypeError("Filter is not set, please use set_filter(filter:function)")
        #algorithm could be optimized by sorting the dataframe only once
        logger.info('first sort')
        rssi_df=self.rssi_df.sort_values('timestamp',ascending=True )
        logger.info('sorted, sampling')
        rssi_df=self.sampling(rssi_df)
        logger.info('sampled,cleaning')

        rssi_df=self.cleaner(self.rssi_df) # type: ignore

        logger.info('cleaned, filtering')

        filtered_df=self.__segmenting(rssi_df)
        
        
        
        return filtered_df
