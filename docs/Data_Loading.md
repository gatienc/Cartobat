### Data Loading

Now that we can get the data from the API, we need to load it into the program. A part of the data will be used few so we will store it in a file to avoid calling the API too often. we will call this kind of data "static data". The other part of the data depends of the time so we will store it in a variable. We will call this kind of data "dynamic data".

`Static data` will be stored in a file in the `data` folder. To save the data in a file. We will use the next functions :

## Static data

### `save_map`

give the name of the map and the API object
will create a csv file in data folder containing the map

data at this format:

| ID_element | coordinates                                                                                                                                                                                                    | nom   |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 21205      | [[244877.66481508993, 6226270.774078507], [244879.45630794036, 6226281.224453468], [244887.07015255472, 6226280.030124901], [244885.42795077516, 6226269.467781637], [244877.66481508993, 6226270.774078507]]  | 4A101 |
| 21264      | [[244952.83286927274, 6226315.3188017765], [244953.91522953653, 6226321.514381218], [244963.0593076273, 6226319.984147741], [244961.93962459578, 6226313.751245532], [244952.83286927274, 6226315.3188017765]] | 4A413 |
| 21265      | [[244951.22799026087, 6226305.055040656], [244951.82515454432, 6226309.123222334], [244961.0065554028, 6226307.592988858], [244960.26010004847, 6226303.524807178], [244951.22799026087, 6226305.055040656]]   | 4A409 |

**Parameters:**

- callAPI: API object
- MapName: str

### `save_cartomodule`

give the name of the map and the API object
will create a csv file in data folder containing the CartoModule of the map

data at this format:

| macModule    | idCouche | coordonneesEPSG3857                     |
| ------------ | -------- | --------------------------------------- |
| A8032A311F96 | 76       | [244950.41442696087,6226334.0893908525] |
| C45BBE39F4D6 | 76       | [244979.34863026388,6226335.888478451]  |
| A8032A311F6A | 76       | [245050.16318292607,6226326.739568699]  |

**Parameters:**

- callAPI: API object
- MapName: str

## Dynamic data

### `ReceiverLoader`

Create a GeoDataFrame from a csv file with coordinates of point
column:geometry -> coordinates in lat/lon
column:coordonneesEPSG3857 -> coordinates in EPSG3857

Parameters

---

Input:
ModuleMapPath: str
the path to the csv file

---

Output:
GeoDataFrame
**Parameters:**

- ModuleMapPath: str
  the path to the csv file

output: GeoDataFrame intial_csv_column+['geometry']

| macModule    | geometry                 |
| ------------ | ------------------------ |
| A8032A31204E | POINT (2.20079 48.71316) |
| C45BBE39F42A | POINT (2.20110 48.71315) |
| C45BBE39F9AE | POINT (2.20120 48.71314) |
| A8032A311FAA | POINT (2.20072 48.71317) |
| C45BBE39F56A | POINT (2.20117 48.71318) |
| C45BBE37B346 | POINT (2.20087 48.71315) |

### `gdfLoader`

Create a GeoDataFrame from a csv file with coordinates of point in a column
add a geometry column with the coordinates

**Parameters:**

- dataPath: str the path to the csv file
- positionColumn: str position column name initial="coordinates"
- dropPositionColumn: bool if true drop the column with the coordinates

output:

| ID_element | nom   | geometry                                          |
| ---------- | ----- | ------------------------------------------------- |
| 21205      | 4A101 | POLYGON ((2.19977 48.71281, 2.19979 48.71287, ... |
| 21264      | 4A413 | POLYGON ((2.20045 48.71307, 2.20046 48.71311, ... |
| 21265      | 4A409 | POLYGON ((2.20043 48.71301, 2.20044 48.71304, ... |
| 21266      |       | POLYGON ((2.20050 48.71315, 2.20055 48.71315, ... |
| 21267      |       | POLYGON ((2.20055 48.71317, 2.20059 48.71316, ... |

### `Receiver`

A class representing a receiver/Mac module in a room. This class has been tought to be the element of a set with mac module id as key.

## **Attributes**:

room : Room
The room in which the receiver is located.
point : Point
The point in the room where the receiver is located.

### `build_receiver_dict`

This function takes a GeoDataFrame of receivers and a list of rooms, and returns a dictionary of the form {macModule: Receiver(room_polygon, receiver_localisation)}.

## **Parameters**:

receiver_gdf : GeoDataFrame
A GeoDataFrame of receivers.
room_list : list
A list of rooms.

## **Returns**:

dict
A dictionary of the form {macModule: Receiver(room_polygon, receiver_localisation)}.

### `Room`

A class representing a room in a building.

## **Attributes**:

uid : int
The unique identifier of the room.
name : Optional[str]
The name of the room (optional).
polygon : Polygon
The polygon representing the shape of the room.

### `room_list_generator`

Generate a list of Room objects from a GeoDataFrame containing room information.

## **Parameters**

Input:
map_gdf: GeoDataFrame
A GeoDataFrame containing room information.

---

**Output**:
list
A list of Room objects.

### `room_r_tree_generator`

Generate an R-tree index from a list of Room objects.

## **Parameters**

Input:
room_list: list
A list of Room objects.

---

**Output**:
rtree.index.Index
An R-tree index containing the Room objects.
