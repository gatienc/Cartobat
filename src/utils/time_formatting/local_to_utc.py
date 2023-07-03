import pytz
import pandas as pd
import os
def local_to_utc(local_time:pd.Timestamp)->pd.Timestamp:
    """Convert local time to UTC time.

    Parameters
    ----------
    local_time : datetime.datetime
        Local time.

    Returns
    -------
    datetime.datetime
        UTC time.

    """
    tz=pytz.timezone(os.environ['TIMEZONE'])
    local_time = tz.localize(local_time, is_dst=None)
    return local_time.astimezone(pytz.utc)