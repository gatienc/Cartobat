import os
from src.init_config import init_config
from src.API.API import API
from src.utils.time_formatting import local_to_utc, utc_to_local
import pandas as pd
from pytz import timezone

if __name__ == "__main__":
    init_config.init_config()
    print(os.getenv('SITE_URL'))
    callApi=API()
    hour_correction=2
    timestamp=pd.to_datetime("2023-06-22 10:40:00.000000")
    start=local_to_utc(timestamp)
    start=utc_to_local(start)
    print(start)