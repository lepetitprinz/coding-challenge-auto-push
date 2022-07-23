import datetime as dt
for _ in range(3):
    ls = input().split()
    start, end = ls[:3], ls[3:]
    start = dt.datetime.strptime(':'.join(start), '%H:%M:%S')
    end = dt.datetime.strptime(':'.join(end), '%H:%M:%S')
    diff = end - start
    second=diff.total_seconds()
    for i in range(3):
        print(int(second // (60 ** (2 - i))), end=' ')
        second %= (60 ** (2 - i))