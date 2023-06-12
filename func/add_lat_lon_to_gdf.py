####################################################
########## Depreciated should have no use ##########
####################################################



from shapely.geometry import Point
import geopandas as gpd
import pandas as pd
from pyproj import Proj, transform
from pyproj import Transformer



transformer = Transformer.from_crs("EPSG:3857","EPSG:4326")

def transformcoord(coord):
    lon, lat = transformer.transform(coord.x, coord.y)
    return  f'{lat}, {lon}'


def add_lat_lon_to_gdf(gdf):
    gdf["latitude"] = None
    gdf["longitude"] = None
    gdf[['longitude','latitude']]= gdf['geometry'].apply(transformcoord).str.split(', ', expand=True)
    return gdf
