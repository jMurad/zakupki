from datetime import datetime, timedelta


datetm = '06.08.2019 15:26 (МСК+7)'
date = datetm.split(' (')[0]
tz = datetm.split('(')[1][3:-1]
if tz == '':
    tz = 0
else:
    tz = int(tz)
datetm = datetime.strptime(date, '%d.%m.%Y %H:%M')
dt = datetime.now()
timemsk = datetm - timedelta(hours=tz)
razn = dt - timemsk
minutes = round(divmod(razn.total_seconds(), 60)[0])

print(minutes)
print(tz)
print(razn)
print(timemsk)