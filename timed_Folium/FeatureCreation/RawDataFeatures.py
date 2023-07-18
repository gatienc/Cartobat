from datetime import datetime
import matplotlib as mpl
import pandas as pd
import matplotlib.colors as mcolors
import geopandas as gpd
import numpy as np


def RawDataFeatures(rssi_df,MacModuleLocation,cmap=None):
    """
    fonctionne mais la barre de progression affiche des points chaque fois qu'ils sont mis , s'il y a un trou de 10h à 13h , cela va passer le trou plutout que de ne rien afficher

    Parameters
    -------
    MacModuleLocation : dict {macModule_id=[lon,lat]}
    """
    if cmap is None:
        cmap = mpl.colormaps['jet'].resampled(30)
        cmap = mpl.colors.ListedColormap(cmap(np.linspace(0, 1, 30)))
    

    
    features = []
    for index,row in rssi_df.iterrows():
        
        timestamp=row["timestamp"].strftime('%Y-%m-%dT%H:%M:%S')

        
        coordinates=MacModuleLocation[row["macModule"]]
        
        color=cmap(row['rssi']+80)
        hex_color=mcolors.rgb2hex(color)
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [coordinates.x,coordinates.y]
            },
            'properties': {
                'times': [timestamp],
                "icon": 'circle',
                "popup": str(row['rssi']),
                "iconstyle": {
                    # "color": hex_color,
                    "fillColor": hex_color,    
                    "fillOpacity": "0.8",  
                    "radius": str(1*(100+row['rssi']))            
                }}
            }
        features.append(feature)
    return features

