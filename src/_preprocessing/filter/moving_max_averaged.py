from .abstractFilter import abstractFilter
import logging
from .moving_max import moving_max_Filter

logger = logging.getLogger('cartobat')

class moving_max_averaged_Filter(abstractFilter):
    """
    Max average averaged filtering the data

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
        #max average filtering of rssi_df using the window size on the column rssi
        rssi_df=moving_max_Filter(window=self.window).filter(rssi_df)  
        rssi_df['rssi']=rssi_df.rolling(self.window,center=True,min_periods=1,closed='both',on='timestamp').rssi.mean().round(1)#round to 1 decimal (could be changed)

        return rssi_df
    