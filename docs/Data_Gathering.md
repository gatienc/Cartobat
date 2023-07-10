## API Documentation


The `API` class provides methods for interacting with an API and retrieving data. It offers the following methods:

---
#### `getRawDataForCartoWear`

Retrieve the raw data for a given CartoWear tag and save it in a CSV file.
You must provide your local time, Class makes the translation to UTC time for calling the API. If you're not in Europe/Paris Timezone, you must provide the timezone in your .env file.

**Parameters:**

- `MAC_WEAR` (str): The MAC_WEAR of the tag.
  
- `StartTimestamp` (pd.Timestamp): The start timestamp of the data.
  
- `EndTimestamp` (pd.Timestamp): The end timestamp of the data.
- `**kwargs` (optional): Additional keyword arguments.
    - `filepath` (str): If provided, the data will be saved to the given file path.

**Returns:**
- `list`: The raw data if valid, None otherwise.

---

#### `getBuilding`

Retrieve the list of buildings from the API.

**Returns:**

- `list`: The list of buildings if valid, None otherwise.

---

#### `getLayersInBuilding`

Retrieve the list of layers in a building.

**Parameters:**

- `buildingid` (int, optional): The ID of the building. If not provided, the ID of the current building is used.

**Returns:**
- `list`: The list of layers if valid, None otherwise.

---

#### `getAreasInLayer`

Retrieve the list of areas in a layer.

**Parameters:**

- `layerid` (int, optional): The ID of the layer. If not provided, the ID of the current layer is used.

**Returns:**

- `list`: The list of areas if valid, None otherwise.

---

#### `getCartoModuleWithLocationList`

Retrieve the list of tags with their location.

**Returns:**

- `list`: The list of tags with location if valid, None otherwise.

---

Please note that the code snippets are not included here for brevity. For more details and usage examples, please refer to the API documentation.


### Usefull functions
this functions are in utils.save.map.

`get_Map_csv(callAPI,MapName)`
    give the name of the map and the API object
    will create a csv file in data folder containing the map
