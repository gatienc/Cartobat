from .Room import Room

#DEPRECATED use room_dict instead
def room_list_generator(map_gdf):
    """
    Generate a list of Room objects from a GeoDataFrame containing room information.

    Parameters
    ----------
    Input:
    map_gdf: GeoDataFrame
        A GeoDataFrame containing room information.

    -------
    Output:
    list
        A list of Room objects.
    """
    room_list=[]
    for index,row in map_gdf.iterrows():
        uid=row["ID_element"]
        room=Room(int(row["ID_element"]),row["nom"],row["geometry"],row["coordinatesEPSG3857"])
        room_list.append(room)
    return(room_list)
def room_dict_generator(map_gdf):
    """
    Generate a list of Room objects from a GeoDataFrame containing room information.

    Parameters
    ----------
    Input:
    map_gdf: GeoDataFrame
        A GeoDataFrame containing room information.

    -------
    Output:
    list
        A list of Room objects.
    """
    room_dict={}
    for index,row in map_gdf.iterrows():
        uid=row["ID_element"]
        room=Room(int(row["ID_element"]),row["nom"],row["geometry"],row["coordinatesEPSG3857"])
        room_dict[uid]=(room)
    return(room_dict)

def room_r_tree_generator(room_list):
    """
    Generate an R-tree index from a list of Room objects.

    Parameters
    ----------
    Input:
    room_list: list
        A list of Room objects.

    -------
    Output:
    rtree.index.Index
        An R-tree index containing the Room objects.
    """
    import rtree
    idx = rtree.index.Index()
    for room in room_list:
        idx.insert(room.uid, room.cartesian_polygon.bounds)
    return idx
