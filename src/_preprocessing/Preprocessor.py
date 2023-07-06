import pandas as pd
from .filter.abstractFilter import abstractFilter
from .cleaner.abstractCleaner import abstractCleaner
from datetime import timedelta
import logging

logger = logging.getLogger('cartobat')

class Preprocessor:
    def __init__(self,rssi_df,*, sampling_time=None) -> None:
        self.rssi_df=rssi_df
        self.filter=None
        self.cleaner=None
        self.sampling_time= timedelta(seconds=sampling_time) if sampling_time!=None else timedelta(seconds=2)#2 seconds window by default
    def set_cleaner(self,cleaner)->'Preprocessor':
        self.cleaner=cleaner
        return self
    def set_filter(self,filter:abstractFilter)->'Preprocessor':
        self.filter=filter
        return self
    def __segmenting(self,rssi_df):
        mac_module_list=rssi_df['macModule'].unique()
        empty_df = pd.DataFrame(columns=rssi_df.columns)
        filtered_df=empty_df.copy()
        for mac_module in mac_module_list:
            mac_module_rssi=rssi_df[rssi_df['macModule']==mac_module]
            logger.info(f'filtering {mac_module}')
            segment=empty_df.copy()
            previous_time=mac_module_rssi.iloc[0]['timestamp']
            for index,row in mac_module_rssi.iterrows():
                if row['timestamp']-previous_time>100*self.sampling_time:
                    logger.info(f'{segment=}')

                    filtered_df=pd.concat([filtered_df,self.filter(segment)])#type: ignore
                    segment=empty_df.copy()
                else:
                    segment=pd.concat([segment,row])#type: ignore
                previous_time=row['timestamp']
            if not segment.empty : filtered_df=pd.concat([filtered_df,self.filter(segment)])#type: ignore
        
        #sort by timestamp the filtered_df
        filtered_df=filtered_df.sort_values('timestamp') # type: ignore
        return(filtered_df)
    def process(self)->'pd.DataFrame':
        if not issubclass(type(self.cleaner), abstractCleaner):
            print(self.cleaner)
            raise TypeError("Cleaner is not set, please use set_cleaner(cleaner:function)")
        if not issubclass(type(self.filter), abstractFilter):
            raise TypeError("Filter is not set, please use set_filter(filter:function)")
        #algorithm could be optimized by sorting the dataframe only once
        logger.info('first sort')
        rssi_df=self.rssi_df.sort_values('timestamp')
        logger.info('sorted, cleaning')

        rssi_df=self.cleaner(self.rssi_df) # type: ignore

        logger.info('cleaned, filtering')
        filtered_df=self.__segmenting(rssi_df)
        
        
        
        return filtered_df
