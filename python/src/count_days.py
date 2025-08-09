import datetime

def count_days(start_date, end_date):
    date1 = datetime.datetime.strptime(start_date, '%Y.%m.%d')
    date2 = datetime.datetime.strptime(end_date, '%Y.%m.%d')
    delta = date2 - date1
    return delta.days