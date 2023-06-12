


def timed_marker_intensity_set_calculation(marker_gdf:gpd.GeoDataFrame, rssi_df:pd.DataFrame, sampling_time:int=2000,):
    """
    Create a set of dataframes as values and the timestamp as key
    
    Parameters
    ----------
    Input:
    marker_gdf : GeoPandas.GeoDataFrame['timestamp', 'macModule', 'geometry']
    rssi_df : Pandas.DataFrame['timestamp', 'macModule', 'rssi']
    sampling_time : int

    -------
    Output:
    set of dataframes
        GeoPandas.GeoDataFrame['timestamp', 'macModule','rssi', 'geometry']
    """

    #implementation with a list of dataframes ouput
    marker_intensity_gdf_set={}
    sampling_time=pd.Timedelta(sampling_time, unit="ms")
    for current_timestamp in timestamp_list:
        #for each module, we keep only the rssi values between current_timestamp and current_timestamp-sampling_time
        rssi_df_current=rssi_df[(rssi_df["timestamp"] > current_timestamp-sampling_time)&(rssi_df["timestamp"] < current_timestamp)]
        rssi_df_current=rssi_df_current.drop(columns=["timestamp","macModule"]).groupby("macModule").mean()
        marker_intensity_gdf=marker_gdf.merge(rssi_df_current, left_on="macModule", right_on="macModule")
        #mean of the rssi values for each module
        marker_intensity_gdf_set[current_timestamp]=marker_intensity_gdf
    return(marker_intensity_gdf_set)