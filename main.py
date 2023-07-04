import os
from src.init_config import init_config
from src.API.API import API
from src.utils.time_formatting import local_to_utc,utc_to_local
from src.preprocessing.Preprocessor import Preprocessor
from src.preprocessing.cleaner.remove_duplicates import remove_duplicates
from src.preprocessing.filter.filter_by_time import filter_by_time
import pandas as pd
from pytz import timezone

if __name__ == "__main__":
    init_config.init_config()
    print(os.getenv('SITE_URL'))
    callApi=API()
    start="2023-06-22 10:40:00.000000"
    end="2023-06-22 11:30:35.000000"
    data=callApi.getRawDataForCartoWear('C77C2F92664E',pd.to_datetime(start),pd.to_datetime(end))
    print(data)
    
    print(f'{data=}')