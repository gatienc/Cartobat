import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from API import API
from secret import API_KEY,MAC_WEAR

Gatien_API=API(API_KEY)
hour_correction=2
start=pd.to_datetime("2023-06-19 08:00:46.000000")-pd.Timedelta(hour_correction, unit="h")
end=pd.to_datetime("2023-06-19 10:00:00.000000")-pd.Timedelta(hour_correction, unit="h")
Gatien_API.getRawDataForCartoWear(MAC_WEAR,start,end)


data= pd.read_csv("data/manipstatic.csv")

data["timestamp"]=pd.to_datetime(data['timestamp'])
print(data.head(5))
#data=data[(data['timestamp'] > '2023-06-01 09:50:00.000000')&(data['timestamp'] < '2023-06-01 09:55:30.000000')]


test=sns.lineplot(  
    data=data, hue="macModule",
    x="timestamp", y="rssi", markers=True
)
 
plt.xlabel('timestamp')
plt.xticks(rotation=100)
plt.ylabel('rssi')
plt.title('RSSI values for tag ')
plt.legend(loc='upper right', fontsize='large')
plt.show()