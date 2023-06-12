import geopandas as gpd
from shapely.geometry import Point,Polygon

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
    return gdf