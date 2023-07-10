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

The data is first cleaned using the cleaning filter provided by set_cleaner().

The data is then sorted by timestamp.

Then the data is segmented :

   For each MacModule, we're creating a 'segment' dataframe containing only the data of the MacModule and without too much time gap between each data point. (gap < 100*sampling time),  this 'segment' dataframe is then sampled every 'sampling time'.
   
   The sample takes the max received signal intensity during the time interval between two sample.
   
   Then, the segment is filtered using the filter provided by set_filter().

   Finally, the filtered segment is added to the final dataframe.