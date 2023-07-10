import geopandas as gpd
from shapely.geometry import Point,Polygon
import ast
import pandas as pd

def gdfLoader(dataPath:str,positionColumn:str ="coordinates",dropPositionColumn:bool =True)->gpd.GeoDataFrame:
    """
    Create a GeoDataFrame from a csv file with coordinates of point in a column
    add a geometry column with the coordinates
    
    Parameters
    ----------
    Input:
    dataPath: str
    the path to the csv file
    positionColumn: str
    position column name
    dropPositionColumn: bool
    if true drop the column with the coordinates

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
        coords=()
        points =Polygon([[coord[0],coord[1]] for coord in element])    
        gdf["geometry"][index]= points
    #keep only the polygons columns
    if dropPositionColumn:gdf=gdf.drop(columns=[positionColumn])
    #set the crs
    gdf=gdf.set_crs(crs="epsg:3857", allow_override=True)
    gdf.to_crs(epsg=4326, inplace=True)

    return gdf

def ReadMarkerMap(ModuleMapPath):
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
        csvcolumn+['geometry']
    """
    #load the receiver map for selected map and layer
    marker_gdf = gpd.read_file(ModuleMapPath)
    #transform the str defining the list in column coordonneesEPSG3857 into a python list
    marker_gdf["coordonneesEPSG3857"] = marker_gdf["coordonneesEPSG3857"].apply(ast.literal_eval)
    #transform the list of coordinates into points in geometry column
    marker_gdf["geometry"] = marker_gdf["coordonneesEPSG3857"].apply(lambda coords: Point(coords))
    #drop the column coordonneesEPSG3857 and the layer id
    marker_gdf = marker_gdf.drop(columns=["coordonneesEPSG3857","idCouche"])
    #set the crs
    marker_gdf=marker_gdf.set_crs(crs="epsg:3857", allow_override=True)
    # change the projection to lat/lon
    marker_gdf=marker_gdf.to_crs(epsg=4326)
    return marker_gdf

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