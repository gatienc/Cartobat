
from src import API,Preprocessor
from src._preprocessing.cleaner.remove_duplicates import remove_duplicates_Cleaner
from src._preprocessing.filter.moving_average import moving_average_Filter
from src._preprocessing.filter.moving_max import moving_max_Filter
from src._preprocessing.filter.moving_max_averaged import moving_max_averaged_Filter
from src._preprocessing.filter.blank import blank_Filter
import pandas as pd
from pytz import timezone
from src.visualization import filtering_comparator,MapCreation
import plotly.graph_objects as go


from src.DataLoader import MarkerLoader,gdfLoader
if __name__ == "__main__":
        #API call
        callApi=API()
        start="2023-06-22 11:34:00.000000"
        end="2023-06-22 11:50:35.000000"
        raw_data=callApi.getRawDataForCartoWear('C77C2F92664E',pd.to_datetime(start),pd.to_datetime(end))
        print(raw_data)

        #Preprocessing
        sampling_time=0.5
        filter_window='2S'
        preprocessor=Preprocessor(raw_data,sampling_time=sampling_time)
        rssi_df=preprocessor.set_cleaner(remove_duplicates_Cleaner())\
                .set_filter(moving_max_averaged_Filter(filter_window))\
                .process()
        rssi_df.to_csv("data/data.csv")

        
        

        
        
    
    
    

