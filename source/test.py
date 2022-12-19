import datetime

date_time_str = "6/25/2017  8:40:00 PM"
date_time_obj = datetime.datetime.strptime(date_time_str, '%m/%d/%Y %I:%M:%S %p')

date_time_str2 = "11/13/2020  11:55:00 AM"
date_time_obj2 = datetime.datetime.strptime(date_time_str2, '%m/%d/%Y %I:%M:%S %p')

delta = (date_time_obj2-date_time_obj)/100

# print('Date:', delta.date())
# print('Time:', delta.time())
print('Date-time:', delta)
