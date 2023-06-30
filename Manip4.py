import numpy as np
import pandas as pd
import seaborn as sns
from src.API.API import API
from secret import API_KEY
import plotly.graph_objects as go

callApi=API()
hour_correction=2
start=pd.to_datetime("2023-06-22 10:40:00.000000")-pd.Timedelta(hour_correction, unit="h")
end=pd.to_datetime("2023-06-22 11:30:35.000000")-pd.Timedelta(hour_correction, unit="h")

data=callApi.getRawDataForCartoWear('C77C2F92664E',start,end)
print(data)


data=data[data['macModule'] == 'A8032A311F6A']

## heure pleine
# data_4A439=data[(data['timestamp'] > pd.to_datetime("2023-06-22 10:40:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 10:45:35.000000")-pd.Timedelta(hour_correction, unit="h"))]
# data_couloir=data[(data['timestamp'] > pd.to_datetime("2023-06-22 10:45:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 10:50:35.000000")-pd.Timedelta(hour_correction, unit="h"))]
# data_ascenceur=data[(data['timestamp'] > pd.to_datetime("2023-06-22 10:50:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 10:55:35.000000")-pd.Timedelta(hour_correction, unit="h"))]
# data_4A436=data[(data['timestamp'] > pd.to_datetime("2023-06-22 10:55:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 11:04:35.000000")-pd.Timedelta(hour_correction, unit="h"))]
# data_4A438=data[(data['timestamp'] > pd.to_datetime("2023-06-22 11:05:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 11:10:35.000000")-pd.Timedelta(hour_correction, unit="h"))]
# data_4A438_2=data[(data['timestamp'] > pd.to_datetime("2023-06-22 11:10:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 11:17:35.000000")-pd.Timedelta(hour_correction, unit="h"))]

#heure creusé
data_4A439=data[(data['timestamp'] > pd.to_datetime("2023-06-22 10:41:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 10:44:00.000000")-pd.Timedelta(hour_correction, unit="h"))]
data_couloir=data[(data['timestamp'] > pd.to_datetime("2023-06-22 10:46:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 10:49:00.000000")-pd.Timedelta(hour_correction, unit="h"))]
data_ascenceur=data[(data['timestamp'] > pd.to_datetime("2023-06-22 10:51:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 10:54:00.000000")-pd.Timedelta(hour_correction, unit="h"))]
data_4A436=data[(data['timestamp'] > pd.to_datetime("2023-06-22 10:56:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 11:03:00.000000")-pd.Timedelta(hour_correction, unit="h"))]
data_4A438=data[(data['timestamp'] > pd.to_datetime("2023-06-22 11:06:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 11:09:00.000000")-pd.Timedelta(hour_correction, unit="h"))]
data_4A438_2=data[(data['timestamp'] > pd.to_datetime("2023-06-22 11:11:00.000000")-pd.Timedelta(hour_correction, unit="h")) & (data['timestamp'] < pd.to_datetime("2023-06-22 11:16:00.000000")-pd.Timedelta(hour_correction, unit="h"))]




fig = go.Figure()
fig.add_trace(go.Box(y=data_4A439["rssi"],name="4A439",boxpoints='all'))
fig.add_trace(go.Box(y=data_couloir["rssi"],name="couloir",boxpoints='all'))
fig.add_trace(go.Box(y=data_ascenceur["rssi"],name="ascenceur",boxpoints='all'))
fig.add_trace(go.Box(y=data_4A436["rssi"],name="4A436",boxpoints='all'))
fig.add_trace(go.Box(y=data_4A438["rssi"],name="4A438",boxpoints='all'))
fig.add_trace(go.Box(y=data_4A438_2["rssi"],name="4A438_2",boxpoints='all'))

fig.show()

