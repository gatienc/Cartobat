from datetime import datetime
input_format = '%Y-%m-%d %H:%M:%S.%f'
output_format = '%Y-%m-%dT%H:%M:%S'
def TimestampReformat(timestamp):
    '''
    reformat timestamp from %Y-%m-%d %H:%M:%S.%f to %Y-%m-%dT%H:%M:%S
    '''
    dt = datetime.strptime(str(timestamp), input_format)
    new_timestamp = dt.strftime(output_format)
    return new_timestamp