import shapely
import rtree
def intersection(polygon:shapely.geometry.Polygon,room_rtree:rtree.index.Index,room_dict:dict):
    """
    Return the room in which the point is located.
    
    """
    #get the intersector with bounds of the polygon
    intersected_room=list(room_rtree.intersection(polygon.exterior.bounds))
    #verfify wich room really intersect with the polygon
    ## would be possible to directly intersect with the polygon here too
    really_intersected_room=[]
    for receiver_room_uid in intersected_room:
        receiver_room = room_dict[receiver_room_uid]
        intersect=shapely.intersection(polygon,receiver_room.cartesian_polygon)
        if not (intersect.is_empty):
            really_intersected_room.append(receiver_room.cartesian_polygon)
    return(really_intersected_room)
