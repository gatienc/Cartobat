import pandas as pd
import geopandas as gpd
def getMarkerDictList(rssi_df, timestamp_list):
    MarkerDictList = []
    index_count=0
    max_count = len(rssi_df)-1
    #on parcours la liste des timestamp, on fait en sorte de profiter que les données sont triées par timestamp, pour cela on crée un dict avec les macModule en clé et les rssi en valeur pour chaque intervalle de temps
    for timestamp in timestamp_list:
        markerdict={}
        while index_count!= max_count and rssi_df.iloc[index_count]['timestamp'] < timestamp:
            MacModule=rssi_df.iloc[index_count]['macModule']
            #if key does not exist, we create it and add the rssi value
            if MacModule not in markerdict:
                markerdict[MacModule]=[rssi_df.iloc[index_count]['rssi']]
            #if key exist, we add the rssi value
            else:
                markerdict[MacModule].append(rssi_df.iloc[index_count]['rssi'])    
            index_count+=1
        #we calculate the average of the rssi values for each macModule
        for rssi in markerdict.values():
            rssi=sum(rssi)/len(rssi)
        MarkerDictList.append(markerdict)
    return(MarkerDictList)