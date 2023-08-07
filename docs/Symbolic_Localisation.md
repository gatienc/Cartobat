# Symbolic localisation algorithm documentation

The princip of the algorithm is to use the rssi of the receiver to predict the zone in wich the emitter could be for each receiver.
Once the zone for each predictor is predicted, intersection of all the predicted zones define the final predicted zone for the emitter position.

## `ZoneSelector`

The `ZoneSelector` class is used to select the zone in wich the emitter could be according to one receiver.

### init

**Parameters**
room_r_tree:rtree define the rtrees index of the rooms for the building
room_dict:dict define the rooms dictionary of the building (to get the room object from the unique id)

### set_threshold

Set the threshold for the zone selection
**Parameters**

Threshold1:int
Threshold2:int

### set_radius

Set the radius for the zone selection, radius is a float, the unity of the radius is the same as the unity of the distance for web-mercator projection (must develop)
**Parameters**
radius1:float
radius2:float

### ZoneSelector.ZoneSelection

Return the predicted zone for the selected receiver receiving the rssi

**Parameters**

Input:
receiver: Receiver
rssi: int

Output:
List of Polygon
