import pandas as pd
from .filter.abstractFilter import abstractFilter
from .cleaner.abstractCleaner import abstractCleaner
from datetime import timedelta
import logging
import numpy as np

logger = logging.getLogger('cartobat')

class Preprocessor:
    """
    Preprocessor class, used to preprocess the data
    set you're cleaner and filter (with set_cleaner and set_filter),
    before calling process()
    
    args:
        rssi_df: dataframe containing the data to preprocess
        sampling_time: number of seconds between each sample, can be float, if None, base sampling is 0.5 seconds
    
    
    """
    def __init__(self,rssi_df,*, sampling_time=None) -> None:
        self.rssi_df=rssi_df.copy()
        self.filter=None
        self.cleaner=None
        self.sampling_time= timedelta(seconds=sampling_time) if sampling_time!=None else timedelta(seconds=0.5)#0.5 seconds window by default

    def sampling(self,rssi_df):
        """
        Sample the current rssi_df , you must provide a sorted rssi_df by timestamp with data of only one mac_module
        """
        #data must be sorted by timestamp
        sampling_time=self.sampling_time
        min_time=min(rssi_df['timestamp']).round(freq='500L')-sampling_time#round to inferior
        max_time=max(rssi_df['timestamp']).round(freq='500L')+sampling_time#round to superior
        time_range=pd.date_range(min_time,max_time,freq=sampling_time)
        count=0
        sampled_df=pd.DataFrame(columns=rssi_df.columns)
        mac_module=rssi_df['macModule'].iloc[0]

        for i in time_range:
            signal_intensity=np.nan#certainly not the best way to do it

            while count< len(rssi_df) and i>rssi_df['timestamp'].iloc[count]:
                signal_intensity=max(rssi_df['rssi'].iloc[count],signal_intensity)
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
        """
        Segment the rssi_df by mac_module and timestamp
        args:
            rssi_df: dataframe containing the data to segments
        """

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
                
                if (delay> 100*self.sampling_time):
                    print(f'{mac_module_rssi=}')
                    print(f'{delay=}')
                    print(f'{segment=}')
                    filtered_df=self._add_row(filtered_df,self.filter(self.sampling(segment)))#type: ignore
                    segment=empty_df.copy()
                
                temp=pd.DataFrame(row).transpose()
                segment=self._add_row(segment,temp)
                
                previous_time=row['timestamp']
                
            
            if not segment.empty : filtered_df=self._add_row(filtered_df,(self.filter(self.sampling(segment))))


        #sort by timestamp the filtered_df
        filtered_df=filtered_df.sort_values('timestamp',ascending=True,ignore_index=True ) # type: ignore
        return(filtered_df)
    def process(self)->'pd.DataFrame':
        if not issubclass(type(self.cleaner), abstractCleaner):
            raise TypeError("Cleaner is not set, please use set_cleaner(cleaner:function)")
        if not issubclass(type(self.filter), abstractFilter):
            raise TypeError("Filter is not set, please use set_filter(filter:function)")
        #algorithm could be optimized by sorting the dataframe only once
        rssi_df=self.rssi_df
        logger.info('data Cleaning')
        rssi_df=self.cleaner(rssi_df) # type: ignore
        logger.info('cleaned, sorting')
        rssi_df=rssi_df.sort_values('timestamp',ascending=True,ignore_index=True )
        logger.info('sorted, filtering')
        filtered_df=self.__segmenting(rssi_df)
        
        logger.info('filtered')
        
        return filtered_df
