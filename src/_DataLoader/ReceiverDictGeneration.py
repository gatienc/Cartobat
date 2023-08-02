from geopandas import GeoDataFrame
import rtree
from shapely.geometry import Point
from .Receiver import Receiver
def point_room(point:Point,room_rtree:rtree.index.Index,room_dict:dict):
    """
    Return the room in which the point is located.
    
    """
    #adaptet r-tree intersection to real object intersection
    
    intersected_room_iterator=room_rtree.intersection(point.coords[0])
    while intersected_room_iterator:
        receiver_room_uid=next(intersected_room_iterator)
        receiver_room = room_dict[receiver_room_uid]
        if receiver_room.cartesian_polygon.contains(point):
            return(receiver_room)
    raise ValueError("The point is not in any room")

def build_receiver_dict(receiver_gdf:GeoDataFrame,room_dict:dict,room_rtree:rtree.index.Index)->dict:
    """
    This function takes a GeoDataFrame of receivers and a list of rooms, and returns a dictionary of the form {macModule: Receiver(room_polygon, receiver_localisation)}.
    
    Parameters:
    -----------
    receiver_gdf : GeoDataFrame
        A GeoDataFrame of receivers.
    room_dict : dict
        A dict of rooms.
        
    Returns:
    --------
    dict
        A dictionary of the form {macModule: Receiver(room_polygon, receiver_localisation)}.
    """

    #should be optimized
    res={}
    for index,row in receiver_gdf.iterrows():
        receiver_localisation=row["coordinatesEPSG3857"]
        receiver_room=point_room(receiver_localisation,room_rtree,room_dict)    
        res[row["macModule"]]=Receiver(receiver_room,row["geometry"],receiver_localisation)
    return(res)