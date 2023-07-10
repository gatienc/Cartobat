import os

from src import API,Preprocessor
from src._preprocessing.cleaner.remove_duplicates import remove_duplicates_Cleaner
from src._preprocessing.filter.moving_average import moving_average_Filter
from src._preprocessing.filter.moving_max import moving_max_Filter
from src._preprocessing.filter.moving_max_averaged import moving_max_averaged_Filter
from src._preprocessing.filter.blank import blank_Filter
import pandas as pd
from pytz import timezone
from src.visualization import filtering_comparator
import plotly.graph_objects as go

if __name__ == "__main__":
        
        #API call
        callApi=API()
        start="2023-06-22 11:34:00.000000"
        end="2023-06-22 11:36:35.000000"
        raw_data=callApi.getRawDataForCartoWear('C77C2F92664E',pd.to_datetime(start),pd.to_datetime(end))
        
        #Preprocessing
        preprocessor=Preprocessor(raw_data,sampling_time=3)
        timedelta=pd.Timedelta(seconds=20)
        filter_list=[moving_max_Filter(timedelta)]#,,moving_max_averaged_Filter(timedelta)]
        fig=filtering_comparator(preprocessor.set_cleaner(remove_duplicates_Cleaner()) ,filter_list,'A8032A311F6A',show=True)
        
    
    
    

