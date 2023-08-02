import geopandas as gpd
import folium

from multipledispatch import dispatch

def room_FeatureGroup(room_dict:dict)->folium.FeatureGroup:
    """
    Creates a FeatureGroup for the rooms in the given dict.
    To change style, take a look here:
    https://leafletjs.com/reference.html#path

    Args:
    room_dict (dict): A dict containing the rooms.

    Returns:
    room_fg (folium.FeatureGroup): A FeatureGroup containing the rooms.
    lat_avg (float): The average latitude of the rooms.
    lon_avg (float): The average longitude of the rooms.
    """
    room_fg = folium.FeatureGroup(name='Room')
        
    lat_sum,lon_sum=0,0
    for room in room_dict.values():
        center=room.spherical_polygon.centroid
        lon,lat=center.x,center.y
        lat_sum+=lat
        lon_sum+=lon
        polygon_list=[(lat,long) for long,lat in list(room.spherical_polygon.exterior.coords)]
        room_fg.add_child(
            folium.Polygon(
                locations=polygon_list,
                popup=(f'uid ={room.uid} name={room.name}'),#folium.Popup(text)
                color= 'black',
                fill_color='black',
            )
        )
    lat_avg=lat_sum/len(room_dict)
    lon_avg=lon_sum/len(room_dict)
    return room_fg,lat_avg,lon_avg
    

def receiver_FeatureGroup(receiver_dict:dict)->folium.FeatureGroup:
    """
    Creates a FeatureGroup for the receivers in the given dictionary.
    To change style, take a look here:
    https://leafletjs.com/reference.html#path

    Args:
    receiver_dict (dict): A dictionary containing the receivers.

    Returns:
    receiver_fg (folium.FeatureGroup): A FeatureGroup containing the receivers.
    """
    receiver_fg = folium.FeatureGroup(name='Receiver')
    for receiver_name, receiver in receiver_dict.items():
        receiver_fg.add_child(
            folium.CircleMarker(
                [receiver.spherical_point.y,receiver.spherical_point.x],
                radius=1,
                color='red',
                fill_color='red',
                popup=(f'{receiver_name} in room :{receiver.room.uid}'),#folium.Popup(text)
            )
        )
    return receiver_fg
import folium
@dispatch(dict,dict)
def MapCreation(receiver_dict:dict,room_dict:dict)->folium.Map:
    """
    Generates a folium map object with a FeatureGroup for the receivers and a FeatureGroup for the rooms.
    

    Args:
    receiver_dict (dict): A dictionary containing the receivers.
    room_dict (dict): A dict containing the rooms.

    Returns:
    map_object (folium.Map): A folium map object containing the FeatureGroups for the receivers and the rooms.
    """
    receiver_fg=receiver_FeatureGroup(receiver_dict)
    room_fg,lat_avg,lon_avg=room_FeatureGroup(room_dict)
    map_object = folium.Map(location = [lat_avg,lon_avg],max_zoom=30, zoom_start=20,crs="EPSG3857")

    map_object.add_child(room_fg)
    map_object.add_child(receiver_fg)
    map_object.add_child(folium.LayerControl())

    return map_object


def MeanMarkerPosition(marker_gdf):
    long=[x for x in marker_gdf["geometry"].x]
    lat=[y for y in marker_gdf["geometry"].y]
    #get the average of long list
    long= sum(long) / len(long)
    lat= sum(lat) / len(lat)
    location=[lat,long]
    return location
@dispatch(gpd.GeoDataFrame)
def MapCreation(map_gdf:gpd.GeoDataFrame,**kwargs):
    if "marker_gdf" in kwargs:
        marker_gdf=kwargs["marker_gdf"]
    if "marker_gdf" in kwargs and "location" not in kwargs:
        location=MeanMarkerPosition(marker_gdf)
    elif "location" in kwargs:
        location=kwargs["location"]
    else:
        raise TypeError("No location given")
    m = folium.Map(location = location,max_zoom=30, zoom_start=20,crs="EPSG3857")
    tooltip = folium.features.GeoJsonTooltip(fields=['ID_element', 'nom'], 
                                            labels=True,
                                            stick=False,
                                            )
    if "marker_gdf" in kwargs:
        tooltip_marker = folium.features.GeoJsonTooltip(fields=['macModule'], 
                                                labels=True,
                                                stick=False)
    folium.GeoJson(map_gdf, tooltip=tooltip).add_to(m)
    if "marker_gdf" in kwargs:
        folium.GeoJson(marker_gdf, tooltip=tooltip_marker).add_to(m)
    return m

