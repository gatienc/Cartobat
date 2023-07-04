

class Preprocessor:
    def __init__(self,rssi_df) -> None:
        self.rssi_df=rssi_df
        self.filter=None
        self.cleaner=None
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
        if self.filter==None:
            raise Exception("Filter is not set, please use set_filter(filter:function)")
        if self.cleaner==None:
            raise Exception("Cleaner is not set, please use set_cleaner(cleaner:function)")
        self.rssi_df=self.filter(self.rssi_df) # type: ignore
        self.rssi_df=self.cleaner(self.rssi_df) # type: ignore
        return self.rssi_df
