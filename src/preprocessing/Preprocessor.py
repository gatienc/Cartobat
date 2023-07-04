

class Preprocessor:
    def __init__(self,rssi_df,sample_time) -> None:
        self.rssi_df=rssi_df
        self.filter=None
        self.cleaner=None
        self.sample_time=sample_time
    def set_cleaner(self,cleaner:function)->'Preprocessor':
        self.cleaner=cleaner
        return self
    def set_filter(self,filter:function)->'Preprocessor':
        self.filter=filter
        return self
    def format_rssi_df(self)->'Preprocessor':
        raw_rssi_df=self.rssi_df.json()
        return self
    def process(self)->'Preprocessor':
        if not isinstance(self.cleaner, function):
            raise TypeError("Cleaner is not set, please use set_cleaner(cleaner:function)")
 
        if not isinstance(self.cleaner, function):
            raise TypeError("Filter is not set, please use set_filter(filter:function)")
        mac_module_list=self.rssi_df['macModule'].unique()
        for mac_module in mac_module_list:
            self.filter(self.rssi_df[self.rssi_df['mac_module']==mac_module]) # type: ignore
        self.rssi_df=self.cleaner(self.rssi_df) # type: ignore
        self.rssi_df=self.filter(self.rssi_df) # type: ignore
        return self.rssi_df
