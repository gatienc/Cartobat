
from .Receiver import Receiver
def build_receiver_dict(receiver_gdf,room_list,room_rtree):
    """
    This function takes a GeoDataFrame of receivers and a list of rooms, and returns a dictionary of the form {macModule: Receiver(room_polygon, receiver_localisation)}.
    
    Parameters:
    -----------
    receiver_gdf : GeoDataFrame
        A GeoDataFrame of receivers.
    room_list : list
        A list of rooms.
        
    Returns:
    --------
    dict
        A dictionary of the form {macModule: Receiver(room_polygon, receiver_localisation)}.
    """

    #should be optimized
    res={}
    for index,row in receiver_gdf.iterrows():
        receiver_localisation=row["coordinatesEPSG3857"]        
        nearest_room_iterator=room_rtree.nearest(receiver_localisation.coords[0],1)
        receiver_room_uid=next(nearest_room_iterator)
        receiver_room = next((r for r in room_list if r.uid == receiver_room_uid), None)
        # counter=1
        # while not receiver_room.polygon.contains(receiver_localisation):
        #     if counter >= 5:
        #         raise Exception("The receiver "+row["macModule"]+" is not in any room.")
        #     receiver_room_uid=next(nearest_room_iterator)
        #     receiver_room = next((r for r in room_list if r.uid == receiver_room_uid), None)
        #     counter+=1
        res[row["macModule"]]=Receiver(receiver_room,row["geometry"],receiver_localisation)
    return(res)