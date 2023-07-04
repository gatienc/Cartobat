import pandas as pd

class Preprocessor:
    def __init__(self,rssi_df,sampling_time=0.2) -> None:
        self.rssi_df=rssi_df
        self.filter=None
        self.cleaner=None
        self.sampling_time=sampling_time#in seconds
    def set_cleaner(self,cleaner:function)->'Preprocessor':
        self.cleaner=cleaner
        return self
    def set_filter(self,filter:function)->'Preprocessor':
        self.filter=filter
        return self
    def __segmenting(self,rssi_df):
        mac_module_list=rssi_df['macModule'].unique()
        empty_df = pd.DataFrame(columns=rssi_df.columns)
        filtered_df=empty_df.copy()
        for mac_module in mac_module_list:
            mac_module_rssi=rssi_df[rssi_df['mac_module']==mac_module]
            segment=empty_df.copy()
            previous_time=mac_module_rssi.iloc[0]['timestamp']
            for index,row in mac_module_rssi.iterrows():
                if row['timestamp']-previous_time>100*self.sampling_time:
                    filtered_df.append(self.filter(segment,self.sampling_time))#type: ignore
                    segment=empty_df.copy()
                else:
                    segment.append(row)#type: ignore
                previous_time=row['timestamp']
            filtered_df.append(self.filter(segment,self.sampling_time))#type: ignore
        
        #sort by timestamp the filtered_df
        filtered_df=filtered_df.sort_values('timestamp') # type: ignore
        return(filtered_df)
    def process(self)->'pd.DataFrame':
        if not isinstance(self.cleaner, function):
            raise TypeError("Cleaner is not set, please use set_cleaner(cleaner:function)")
        if not isinstance(self.cleaner, function):
            raise TypeError("Filter is not set, please use set_filter(filter:function)")
        #algorithm could be optimized by sorting the dataframe only once
        rssi_df=self.rssi_df.sort_values('timestamp')
        rssi_df=self.__segmenting(rssi_df)
        rssi_df=self.cleaner(self.rssi_df) # type: ignore
        
        
        return filtered_df
