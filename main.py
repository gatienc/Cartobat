import os

from src import API
import pandas as pd
from pytz import timezone

if __name__ == "__main__":
    print(os.getenv('SITE_URL'))
    callApi=API()
    start="2023-06-22 10:40:00.000000"
    end="2023-06-22 11:30:35.000000"
    data=callApi.getRawDataForCartoWear('C77C2F92664E',pd.to_datetime(start),pd.to_datetime(end))
    print(data)
    
    print(f'{data=}')