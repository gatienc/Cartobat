import pytz
import os
import pandas as pd
import datetime
from zoneinfo import ZoneInfo


def utc_to_local(utc_time:pd.Timestamp)->pd.Timestamp:
    """Convert UTC time to local time.

    Parameters
    ----------
    utc_time : datetime.datetime
        UTC time.
    timezone : str, optional
        Timezone, by default 'Europe/Paris'.

    Returns
    -------
    datetime.datetime
        Local time.

    """
    try:#sometimes the timestamp is not in the right format (no milliseconds)
        datetime_obj = datetime.datetime.strptime(str(utc_time), '%Y-%m-%d %H:%M:%S.%f')
    except:
        datetime_obj = datetime.datetime.strptime(str(utc_time), '%Y-%m-%d %H:%M:%S')
    
    tz=os.environ['TIMEZONE']
    timezone=pytz.timezone(tz)
    # Convert the localized datetime to UTC
    local_datetime = datetime_obj.astimezone(timezone)
    return local_datetime