import pytz

def local_to_utc(local_time):
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
    return local_time.astimezone(pytz.utc) 
