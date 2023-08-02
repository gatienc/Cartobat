import geopandas as gpd
from shapely.geometry import Point,Polygon
import ast
import pandas as pd
from . import Receiver

def gdfLoader(dataPath:str,positionColumn:str ="coordinates")->gpd.GeoDataFrame:
    """
    Create a GeoDataFrame from a csv file with coordinates of point in a column
    initial coordinates use mercator projection/ pseudo mercator projection crs: (EPSG:3857)

    column:geometry -> coordinates in lat/lon
    column:coordonneesEPSG3857 -> coordinates in EPSG3857
    
     
    Parameters
    ----------
    Input:
    dataPath: str
    the path to the csv file
    positionColumn: str
    position column name


    -------
    Output:
    GeoDataFrame
        csvcolumn+['geometry']
    """
    #load data
    gdf = gpd.read_file(dataPath)
    #from coordinates to polygon
    for index,element in enumerate(gdf[positionColumn]):
        element=eval(element)
        points =Polygon([[coord[0],coord[1]] for coord in element])    
        gdf["geometry"][index]= points
    gdf.set_crs(crs="epsg:3857", inplace=True)
    gdf.drop(columns=positionColumn,inplace=True)

    gdf["coordinatesEPSG3857"]=gdf["geometry"]
    #set the crs
    gdf.to_crs(epsg=4326, inplace=True)

    return gdf

def ReceiverLoader(ModuleMapPath,coordinatesEPSG3857_column:str="coordonneesEPSG3857")->gpd.GeoDataFrame:
    """
    Create a GeoDataFrame from a csv file with coordinates of point in column:coordonneesEPSG3857
    add a geometry column with the coordinates and transfer it to lat/lon
    
    Parameters
    ----------
    Input:
    ModuleMapPath: str
    the path to the csv file
    
    -------
    Output:
    GeoDataFrame
        csvcolumn+['geometry']+coordonneesEPSG3857
    """
    #load the receiver map for selected map and layer
    receiver_gdf = gpd.read_file(ModuleMapPath)
    #transform the str defining the list in column coordonneesEPSG3857 into a python list
    receiver_gdf[coordinatesEPSG3857_column] = receiver_gdf[coordinatesEPSG3857_column].apply(ast.literal_eval)
    #transform the list of coordinates into points in geometry column
    receiver_gdf["geometry"] = receiver_gdf[coordinatesEPSG3857_column].apply(lambda coords: Point(coords))
    #set the crs
    receiver_gdf=receiver_gdf.set_crs(crs="epsg:3857", allow_override=True)
    #drop the column coordonneesEPSG3857 and the layer id
    receiver_gdf["coordinatesEPSG3857"]=receiver_gdf["geometry"]

    receiver_gdf = receiver_gdf.drop(columns=["idCouche","coordonneesEPSG3857"])
    # change the projection to lat/lon
    receiver_gdf=receiver_gdf.to_crs(epsg=4326)
    return receiver_gdf

# Deprecated
# Should call API instead of loading from file
def RSSIDataLoader(Data_Path):
    """
    Load the rssi data from the csv file and return a dataframe with the timestamp as index
    
    Parameters
    ----------
    Input:
    Data_Path: str
    the path to the csv file

    -------
    Output:
    DataFrame
        csv sorted by timestamp
    """
    #load the received rssi data
    rssi_df = pd.read_csv(Data_Path)
    #timestamp is a string, we need to convert it to datetime
    rssi_df["timestamp"] = pd.to_datetime(rssi_df["timestamp"])
    # set the timestamp as index
    rssi_df=rssi_df.sort_values('timestamp')
    #drop the duplicates
    rssi_df=rssi_df.drop_duplicates()
    rssi_df.index = pd.RangeIndex(len(rssi_df.index))
    return rssi_df