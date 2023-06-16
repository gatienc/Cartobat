def TimedMarkerIntensityList(rssi_df, sampling_time):
    min_timestamp=rssi_df.iloc[0]['timestamp']+pd.Timedelta(sampling_time, unit="ms")
    max_timestamp=rssi_df.iloc[-1]['timestamp']
    timestamp_list= pd.date_range(start=min_timestamp, end=max_timestamp, freq=str(sampling_time)+"ms").tolist()
    #implementation with a list of dataframes ouput
    marker_intensity_gdf_list=[]
    sampling_time=pd.Timedelta(sampling_time, unit="ms")
    for current_timestamp in timestamp_list:
        #for each module, we keep only the rssi values between current_timestamp and current_timestamp-sampling_time
        rssi_df_current=rssi_df[(rssi_df["timestamp"] > current_timestamp-sampling_time)&(rssi_df["timestamp"] < current_timestamp)]
        rssi_df_current=rssi_df_current.drop(columns=["timestamp","macModule"]).groupby("macModule").mean()
        marker_intensity_gdf=marker_gdf.merge(rssi_df_current, left_on="macModule", right_on="macModule")
        #mean of the rssi values for each module
        marker_intensity_gdf_list.append(marker_intensity_gdf)
    return(marker_intensity_gdf_list)