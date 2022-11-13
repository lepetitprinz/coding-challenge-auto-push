import datetime

n, k = map(int, input().split())
day = {}
time = [(0,datetime.datetime(1,1,1,15,0,0)), (0,datetime.datetime(1,1,1,18,0,0)), (0,datetime.datetime(1,1,1,21,0,0))]
day[0] = [f'{str(time[0][1].hour).zfill(2)}:{str(time[0][1].minute).zfill(2)}',
          f'{str(time[1][1].hour).zfill(2)}:{str(time[1][1].minute).zfill(2)}',
          f'{str(time[2][1].hour).zfill(2)}:{str(time[2][1].minute).zfill(2)}']

for i in range(1, n+1):
    for j in range(3):
        d, t = time[j]
        before = t
        t = t + datetime.timedelta(minutes=k)
        if t.hour == 0 and before.hour != t.hour:
            d += 2
        else:
            d += 1
            
        time[j] = [d, t]
        if day.get(d, 0):
            day[d].append(f'{str(t.hour).zfill(2)}:{str(t.minute).zfill(2)}')
        else:
            day[d] = [f'{str(t.hour).zfill(2)}:{str(t.minute).zfill(2)}']

print(len(day[n]))
print(*day[n], sep='\n')