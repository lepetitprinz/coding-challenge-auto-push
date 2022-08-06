import datetime as dt

from_day = list(map(str, input().split()))
to_day = list(map(str, input().split()))

from_day_str = from_day[0].zfill(4) + from_day[1].zfill(2) + from_day[2].zfill(2)
to_day_str = to_day[0].zfill(4) + to_day[1].zfill(2) + to_day[2].zfill(2)
max_day_str = str(int(from_day[0]) + 1000) + from_day[1].zfill(2) + from_day[2].zfill(2)

from_datetime = dt.datetime.strptime(from_day_str, '%Y%m%d')
to_datetime = dt.datetime.strptime(to_day_str, '%Y%m%d')
max_datetime = dt.datetime.strptime(max_day_str, '%Y%m%d')

max_diff = max_datetime - from_datetime
max_diff_day = max_diff.days
diff = to_datetime - from_datetime
diff_day = diff.days

if diff_day >= max_diff_day:
    print('gg')
else:
    print(f'D-{diff_day}')