# Preprocessing Documentation

The `Preprocessing` class provides methods for preprocessing the data. Cleaning refer to the process of removing invalid data points, while filtering refers to the process of trying to reconstruct the RSSI signal received by a MacModule.

__Cleaning__ applies on the __whole__ dataset, while __filtering__ applies on __each MacModule__ data.


## Filtering

The raw rssi data comes in the form of :

| timestamp                        | macModule    | rssi |
| -------------------------------- | ------------ | ---  |
| 2023-06-22 09:30:32.833000+02:00 | A8032A311F96 | -76  |
| 2023-06-22 09:30:27.755000+02:00 | A8032A311F6A | -70  |
| 2023-06-22 09:30:27.755000+02:00 | A8032A30FB9E | -70  |
| -------------------------------- | ------------ | ---  |
| 2023-06-22 08:40:11.082000+02:00 | A8032A311F96 | -72  |
| 2023-06-22 08:40:10.954000+02:00 | A8032A311F6A | -64  |
| 2023-06-22 08:40:08.524000+02:00 | A8032A311F96 | -75  |

The filtering process is done in 3 steps:

1. __Isolate__ the data of each MacModule
2. __Apply__ a given __filter__ on the RSSI values (mean average, high enveloppe, Kalman filter)
3. __Sample__ the filtered data every "sampling time".