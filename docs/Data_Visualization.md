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


## map viz