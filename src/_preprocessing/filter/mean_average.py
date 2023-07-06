from .abstractFilter import abstractFilter
class mean_average_Filter(abstractFilter):
    """
    Mean average filtering the data

    Args:
        window : Size of the moving window
        If an integer, the fixed number of observations used for each window.

        If a timedelta, str, or offset, the time period of each window. Each window will be a variable sized based on the observations included in the time-period. This is only valid for datetimelike indexes
        
            For more information, see the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html).
    Returns:
        pd.dataframe: Filtered Data
    """
    def __init__(self,window):
      self.window = window
    def filter(self, rssi_df):
        print(rssi_df)
        rssi_df=rssi_df.rolling(self.window).mean('rssi')
        #rssi_df.mean()
        return rssi_df
    