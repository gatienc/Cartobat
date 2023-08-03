import folium
from folium.plugins import TimestampedGeoJson
import shapely
# feature = {
#     'type': 'Feature',
#     'geometry': {
#         'type': 'Point',
#         'coordinates': [coordinates.x,coordinates.y]
#     },
#     'properties': {
#         'times': [timestamp],
#         "icon": 'circle',
#         "popup": str(row['rssi']),
#         "iconstyle": {
#             # "color": hex_color,
#             "fillColor": hex_color,    
#             "fillOpacity": "0.8",  
#             "radius": str(1*(100+row['rssi']))            
#         }}
#     }
from datetime import datetime
def timestamp_transform(timestamp:str)->str:
    input_format = '%Y-%m-%d %H:%M:%S'
    input_format2 = '%Y-%m-%d %H:%M:%S.%f'
    output_format = '%Y-%m-%d %H:%M:%S.%f'
    try:
        dt = datetime.strptime(str(timestamp), input_format)
    except ValueError:
        dt = datetime.strptime(str(timestamp), input_format2)
    new_timestamp = dt.strftime(output_format)
    return(new_timestamp)
def list_(*args): return list(args)

def polygon_timed_feature(polygon:shapely.geometry.Polygon,timestamp:str):
    timestamp=timestamp_transform(timestamp)
    
    feature={
        'type': 'Feature',
        'geometry': {
            'type': 'Polygon',
            'coordinates': [[[y,x] for (x,y) in polygon.exterior.coords]]
        },
        'properties': {
            'times': [timestamp],
        }
        }
    return(feature)
def multipolygon_timed_feature(multipolygon:shapely.geometry.MultiPolygon,timestamp:str):
    timestamp=timestamp_transform(timestamp)
    feature={
        'type': 'Feature',
        'geometry': {
            'type': 'MultiPolygon',
            'coordinates': [[[[y,x] for (x,y) in polygon.exterior.coords]] for polygon in multipolygon.geoms]
        },
        'properties': {
            'times': [str(timestamp)],
        }}
    return(feature)
        
def timed_room_Feature(polygon_dict:dict)->folium.FeatureGroup:
    """
    return a FeatureGroup with the polygon from polygon_dict values
    
    """
    features=[]
    for timestamp,polygon in polygon_dict.items():
        if isinstance(polygon,shapely.geometry.Polygon):
            feature=polygon_timed_feature(polygon,timestamp)
        if isinstance(polygon,shapely.geometry.MultiPolygon):
            feature=multipolygon_timed_feature(polygon,timestamp)
        if feature:
            features.append(feature)
    return(features)