from .abstractFilter import abstractFilter
import logging

logger = logging.getLogger('cartobat')

class blank_Filter(abstractFilter):
    """
    not filtering the data, for testing purposes

       Returns:
        pd.dataframe: Filtered Data
    """
    def __init__(self):
        pass
    def filter(self, rssi_df):
        return rssi_df
    