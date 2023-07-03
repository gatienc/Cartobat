import pytz
def utc_to_local(utc_time, timezone='Europe/Paris'):
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
    return utc_time.astimezone(pytz.timezone(timezone))