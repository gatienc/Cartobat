import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
data= pd.read_csv("data/manipstatic.csv")
data["timestamp"]=pd.to_datetime(data['timestamp'])
# data=data[(data['timestamp'] > '2023-06-01 09:50:00.000000')&(data['timestamp'] < '2023-06-01 09:55:30.000000')]
data=data.drop('timestamp', axis=1)
print(data.head(5))


test=sns.barplot(  
    data=data,
    x="macModule", y="rssi"
)
 
plt.xlabel('timestamp')
plt.xticks(rotation=100)
plt.ylabel('rssi')
plt.title('RSSI values for tag ')
plt.legend(loc='upper right', fontsize='large')
plt.show()

#group by macModule then mean of rssi
data=data.groupby(['macModule']).mean()
data=data.reset_index()
print(data.head(5))