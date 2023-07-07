import os

from src import API,Preprocessor
from src._preprocessing.cleaner.remove_duplicates import remove_duplicates_Cleaner
from src._preprocessing.filter.mean_average import mean_average_Filter
from src._preprocessing.filter.max_average import max_average_Filter
from src._preprocessing.filter.max_average_averaged import max_average_averaged_Filter
import pandas as pd
from pytz import timezone
from src._preprocessing.Preprocessor import Preprocessor
from src._visualization.filter_comparison import add_line_plot
import plotly.graph_objects as go

if __name__ == "__main__":
    print(os.getenv('SITE_URL'))
    callApi=API()
    start="2023-06-22 11:39:00.000000"
    end="2023-06-22 12:30:35.000000"
    raw_data=callApi.getRawDataForCartoWear('C77C2F92664E',pd.to_datetime(start),pd.to_datetime(end))

    preprocessor=Preprocessor(raw_data,sampling_time=3)
    mean_average_data=preprocessor.set_cleaner(remove_duplicates_Cleaner())\
                .set_filter(mean_average_Filter(20))\
                .process()
    max_average_data=preprocessor.set_cleaner(remove_duplicates_Cleaner())\
                .set_filter(max_average_Filter(20))\
                .process()
    max_average_averaged_data=preprocessor.set_cleaner(remove_duplicates_Cleaner())\
            .set_filter(max_average_averaged_Filter(20))\
            .process()
    
    fig = go.Figure()
    
    
    fig=add_line_plot(raw_data,fig, 'macModule', 'A8032A311F6A', 'timestamp', 'rssi', 'raw_data')
    fig=add_line_plot(mean_average_data,fig, 'macModule', 'A8032A311F6A', 'timestamp', 'rssi', 'mean_average_Filter')
    fig=add_line_plot(max_average_data,fig, 'macModule', 'A8032A311F6A', 'timestamp', 'rssi', 'max_average_Filter')
    fig=add_line_plot(max_average_averaged_data,fig, 'macModule', 'A8032A311F6A', 'timestamp', 'rssi', 'max_average_Filter')

    fig.show()
    
    
    

