import os

from src import API,Preprocessor
from src._preprocessing.cleaner.remove_duplicates import remove_duplicates_Cleaner
from src._preprocessing.filter.mean_average import mean_average_Filter
import pandas as pd
from pytz import timezone
from src._preprocessing.Preprocessor import Preprocessor
if __name__ == "__main__":
    print(os.getenv('SITE_URL'))
    callApi=API()
    start="2023-06-22 10:40:00.000000"
    end="2023-06-22 11:30:35.000000"
    data=callApi.getRawDataForCartoWear('C77C2F92664E',pd.to_datetime(start),pd.to_datetime(end))

    print('data loaded')
    my_filter=mean_average_Filter(20)
    my_cleaner=remove_duplicates_Cleaner()
    print('filter and cleaner loaded')

    preprocessor=Preprocessor(data,sampling_time=3)
    print('preprocessor loaded')
    preprocessor.set_cleaner(my_cleaner)
    print('cleaner set')
    preprocessor.set_filter(my_filter)
    print('filter set')
    data=preprocessor.process()
    print('preprocessing done')
    print(data)