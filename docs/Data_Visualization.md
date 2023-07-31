# Vizualisation Documentation

## graph viz

`filtering_comparator`

This function is used to compare the effect of different filters on the same data
cleaner must have been set before calling this function

**Parameters:**

- preprocessor (Preprocessor): The preprocessor to use (cleaner must have been set)
- filter_list (list): The list of filters to compare
  mac_module_id (str): The mac module id to plot
- show (bool, optional): If true show the plot. Defaults to False.
- name_list (list, optional): The list of names to use for the filters. Defaults to None.

**Returns:**

- fig (plotly.graph_objects.Figure): The figure containing the plot

---

`rssi_viewer`

This function is used to visualize the rssi data of every mac_module in the rssi_df

**Parameters:**

- rssi_df (pandas.dataframe ): The rssi_df to visualize

```plotly
{"file_path": "./plotly/rssi_viewer.json"}
```

## map viz

`MapCreation`
Generates a folium map object with a FeatureGroup for the receivers and a FeatureGroup for the rooms.

Args:
receiver_dict (dict): A dictionary containing the receivers.
room_list (list): A list containing the rooms.

Returns:
map_object (folium.Map): A folium map object containing the FeatureGroups for the receivers and the rooms.

`receiver_FeatureGroup`
Creates a FeatureGroup for the receivers in the given dictionary.
To change style, take a look here:
https://leafletjs.com/reference.html#path

Args:
receiver_dict (dict): A dictionary containing the receivers.

Returns:
receiver_fg (folium.FeatureGroup): A FeatureGroup containing the receivers.

`room_FeatureGroup`

Creates a FeatureGroup for the rooms in the given list.
To change style, take a look here:
https://leafletjs.com/reference.html#path

Args:
room_list (list): A list containing the rooms.

Returns:
room_fg (folium.FeatureGroup): A FeatureGroup containing the rooms.
lat_avg (float): The average latitude of the rooms.
lon_avg (float): The average longitude of the rooms.
