from datetime import datetime
import matplotlib as mpl
import matplotlib.colors as mcolors

def RawDataFeatures(MarkerDictList,timestamp_list,MacModuleLocation,cmap):
    input_format = '%Y-%m-%d %H:%M:%S.%f'
    output_format = '%Y-%m-%dT%H:%M:%S'
    pointList=[]
    MarkerTimestamplist=[]
    rssiList=[]
    for index,timestamp in enumerate(timestamp_list):
        dt = datetime.strptime(str(timestamp), input_format)
        new_timestamp = dt.strftime(output_format)
        for MarkerDict in MarkerDictList[index]:
                point=MacModuleLocation[MarkerDict]
                pointList.append([point.x,point.y])
                MarkerTimestamplist.append(new_timestamp)
                rssiList.append(MarkerDictList[index][MarkerDict])

    features = []
    for index in range(len(pointList)):
        rgb_list=cmap(rssiList[index]+80)
        hex_color=mcolors.rgb2hex(rgb_list)
        print([MarkerTimestamplist[index]])
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': pointList[index]
            },
            'properties': {
                'times': [MarkerTimestamplist[index]],
                "icon": 'circle',
                "popup": str(rssiList[index]),
                "iconstyle": {
                    "color": hex_color,
                    "fillColor": hex_color,    
                    "fillOpacity": "0.8",  
                    "radius": str(1*(80+rssiList[index]))            
                }}
            }
        features.append(feature)
    return features
