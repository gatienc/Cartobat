import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from API import API
from secret import API_KEY,MAC_WEAR

Gatien_API=API(API_KEY)
hour_correction=2
start=pd.to_datetime("2023-06-22 10:40:00.000000")-pd.Timedelta(hour_correction, unit="h")
end=pd.to_datetime("2023-06-22 11:30:35.000000")-pd.Timedelta(hour_correction, unit="h")
data=Gatien_API.getRawDataForCartoWear(MAC_WEAR,start,end)
data=pd.DataFrame(data)
data=data[data['macModule'] == 'A8032A311F6A']

data["timestamp"]=pd.to_datetime(data['timestamp'])
#apply rolling mean on the rssi values
data['rssi']=data['rssi'].rolling(10).mean()


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