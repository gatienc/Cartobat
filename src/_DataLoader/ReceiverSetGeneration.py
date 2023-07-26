
from .Receiver import Receiver
def build_receiver_set(receiver_gdf,room_list,room_rtree):
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
    ## could be optimised by using a dictionary instead of a list of rooms ( will be faster)

    res={}
    for index,row in receiver_gdf.iterrows():
        receiver_localisation=row["geometry"]
        for i in room_rtree.intersection(receiver_localisation.bounds):     
            receiver_room=[room for room in room_list if room.uid == i]
            if len(receiver_room)>1:
                raise ValueError(f"Macmodule in Multiple room error:\n macmodule:{row['macModule']}\n receiver_localisation:{receiver_localisation}\n receiver_room:{receiver_room}")
            else:
                receiver_room=receiver_room[0]
                res[row["macModule"]]=Receiver(receiver_room,receiver_localisation)
    return(res)