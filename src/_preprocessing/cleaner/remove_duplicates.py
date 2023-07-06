from .abstractCleaner import abstractCleaner
class remove_duplicates_Cleaner(abstractCleaner):
    """
    Clean the data by removing the rows that are duplicated

     Returns:
        pd.dataframe: Filtered Data
    """
    def __init__(self):
        pass
    def cleaner(self, df):
        """
        Clean the rssi_df by removing the rows that are too close in time
        """

        df_unique = df.drop_duplicates()

        return df_unique
