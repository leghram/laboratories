from datetime import datetime, timedelta


def get_dates_in_interval(start_date, end_date):
    result = []
    if start_date is None or end_date is None:
        return
    if start_date == end_date:
        return [start_date]

    # TODO: Solve normal use case
    interval = timedelta(days=1)
    range_dates = (datetime.strptime(end_date, '%m/%d/%Y') - datetime.strptime(start_date, '%m/%d/%Y')).days

    for position in range(range_dates):
        result.append(str((datetime.strptime(start_date, '%m/%d/%Y') + interval*position).date()))
    
    return result

