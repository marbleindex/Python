from datetime import datetime, timedelta #import datetime modules, timedelta

log = ['[16/Aug/2017:18:23:40']


datetime_object = datetime.strptime(log[0], '[%d/%b/%Y:%H:%M:%S') # use strptime module and set the new format
today =  datetime.today()  # use today method
midnight = datetime.combine(today, datetime.min.time()) # use combine method with parameters

print(type(datetime_object))
print(midnight)

print(datetime_object)  # printed in default format
elapsed = today - datetime_object
print(elapsed.seconds)

tdelta = datetime.timedelta(days=7) # set a timedelta of 7 days

print(tday - tdelta)

date2 = date1 + timedelta
timedelta = date1 + date2

bday = datetime.date(2016,9,24) # determines birthday

till_bday = bday - tday # calculates days between birthday and today

print(till_bday.seconds)

print(today)
