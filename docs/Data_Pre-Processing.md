# Preprocessing Documentation

The `Preprocessing` class provides methods for preprocessing the data. Cleaning refer to the process of removing invalid data points, while filtering refers to the process of trying to reconstruct the RSSI signal received by a MacModule.

__Cleaning__ applies on the __whole__ dataset, while __filtering__ applies on __each MacModule__ data.
## Cleaning

You can provide you're own cleaning function to the `Preprocessing` class. The function must be a child of the `abstractCleaner` class and overriding cleaning method.
The `Preprocessing` class will then apply the function on the whole dataset.

The current cleaning method implemented are:

---
### `remove_duplicates_Cleaner`

Clean the data by removing the rows that are duplicated

**Returns:**

- pd.dataframe: Filtered Data
  
---

## Filtering

The filtering process is done in 3 steps:

1. __Isolate__ the data of each MacModule (algoritmic optimization non-include)
2. __Sample__ the filtered data every "sampling time".
3. __Apply__ a given __filter__ on the RSSI values (mean average, high enveloppe, Kalman filter)

[detailed explanation of the Preprocessing workflow](Detailed-Pre-processing.md)


The current filtering method implemented are:

---

### `moving_average_Filter:`


Apply a moving average filter on the data

For more information about the moving average filter, see the [Wikipedia page](https://en.wikipedia.org/wiki/Moving_average)

**Parameters:**

    window: Size of the window used for the moving average filter (in delay)
    
```plotly
{"file_path": "./plotly/moving_average.json"}
```

### `moving_max_Filter:`

Apply a moving max filter on the data, similar to the moving average filter but using the max value instead of the mean


**Parameters:**

    window: Size of the window used for the moving average filter (in delay)

    
```plotly
{"file_path": "./plotly/moving_max.json"}
```

### `moving_max_average_Filter:`

Apply a moving max average filter on the data, the filter first apply a moving max filter and then a moving average filter on the data, it allows to smooth the data while keeping the max value. It gives a satisfaisant high enveloppe of the data.

**Parameters:**

    window: Size of the window used for the moving average filter (in delay)

```plotly
{"file_path": "./plotly/moving_max_averaged.json"}
```
