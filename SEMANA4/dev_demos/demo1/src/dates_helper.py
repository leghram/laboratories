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


def get_default_date_data(start_date, end_date,default_value):
  if start_date==None or end_date == None or datetime.strptime(start_date, '%m/%d/%Y') > datetime.strptime(end_date, '%m/%d/%Y'):
    return []
  if datetime.strptime(start_date, '%m/%d/%Y') == datetime.strptime(end_date, '%m/%d/%Y'):
    return [
      {
        'date':start_date,
        'participants':default_value
      }
    ]
  date_list = []
  interval = timedelta(days=1)
  range_dates = (datetime.strptime(end_date, '%m/%d/%Y') - datetime.strptime(start_date, '%m/%d/%Y')).days
  for position in range(range_dates):
    date_list.append(
        {
        'date':str((datetime.strptime(start_date, '%m/%d/%Y') + interval*position).date()),
        'participants':default_value
        }
    )
  return date_list