### Data Loading

Now that we can get the data from the API, we need to load it into the program. A part of the data will be used few so we will store it in a file to avoid calling the API too often. we will call this kind of data "static data". The other part of the data depends of the time so we will store it in a variable. We will call this kind of data "dynamic data".

`Static data` will be stored in a file in the `data` folder. To save the data in a file. We will use the next functions :



## Static data

### `save_map`

give the name of the map and the API object
will create a csv file in data folder containing the map

data at this format:

| ID_element | coordinates | nom   |
|-----------|--------------------|-------|
| 21205     | [[244877.66481508993, 6226270.774078507], [244879.45630794036, 6226281.224453468], [244887.07015255472, 6226280.030124901], [244885.42795077516, 6226269.467781637], [244877.66481508993, 6226270.774078507]] | 4A101 |
| 21264     | [[244952.83286927274, 6226315.3188017765], [244953.91522953653, 6226321.514381218], [244963.0593076273, 6226319.984147741], [244961.93962459578, 6226313.751245532], [244952.83286927274, 6226315.3188017765]] | 4A413 |
| 21265     | [[244951.22799026087, 6226305.055040656], [244951.82515454432, 6226309.123222334], [244961.0065554028, 6226307.592988858], [244960.26010004847, 6226303.524807178], [244951.22799026087, 6226305.055040656]] | 4A409 |

**Parameters:**

- callAPI: API object
- MapName: str
  

### `save_cartomodule`

give the name of the map and the API object
will create a csv file in data folder containing the CartoModule of the map

data at this format:

| macModule                        | idCouche    | coordonneesEPSG3857 |
| -------------------------------- | ------------ | ---  |
| A8032A311F96 | 76 | [244950.41442696087,6226334.0893908525]  |
|C45BBE39F4D6 | 76 | [244979.34863026388,6226335.888478451]  |
| A8032A311F6A | 76 | [245050.16318292607,6226326.739568699]  |


**Parameters:**

- callAPI: API object
- MapName: str

## Dynamic data

### `ReadMarkerMap`

Create a GeoDataFrame from a csv file with coordinates of point in column:coordonneesEPSG3857
add a geometry column with the coordinates and transfer it to latitude / longitude


output:

|   macModule   |      geometry       |
|--------------|---------------------|
| A8032A31204E | POINT (2.20079 48.71316) |
| C45BBE39F42A | POINT (2.20110 48.71315) |
| C45BBE39F9AE | POINT (2.20120 48.71314) |
| A8032A311FAA | POINT (2.20072 48.71317) |
| C45BBE39F56A | POINT (2.20117 48.71318) |
| C45BBE37B346 | POINT (2.20087 48.71315) |

  
**Parameters**
----------
*Input:* _ModuleMapPath: str
the path to the csv file

-------
*Output:* GeoDataFrame
    csvcolumn+['geometry']


### gdfLoader

Create a GeoDataFrame from a csv file with coordinates of point in a column
add a geometry column with the coordinates
    