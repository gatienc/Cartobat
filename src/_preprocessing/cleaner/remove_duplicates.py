def remove_duplicates(df):
    """
    Clean the rssi_df by removing the rows that are too close in time
    """

    df_unique = df.drop_duplicates()

    return df_unique