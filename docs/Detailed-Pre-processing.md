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

- Clean the data using the cleaning Filter provided by set_cleaner()
- Sort the data by timestamp
- Merge the dataframes of each MacModule into one dataframe

Segmenting


Segment the data :
   For each MacModule, create a dataframe containing only the data of the MacModule and without too much time gap between each data point. (gap < 100*sampling time),
   it optimize the filtering process by reducing the number of data point to filter. Then for each sub-dataframe:

   1. Sample the data every "sampling time"
   2. Filter the data using the filter provided by set_filter()