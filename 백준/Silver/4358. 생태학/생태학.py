import sys

tot_cnt = 0
data = {}
for line in sys.stdin:
    if line == '\n':
        break
    name = line.rstrip()
    tot_cnt += 1
    if name in data:
        data[name] += 1
    else:
        data[name] = 1

        
data_sorted = sorted(data.items(), key=lambda x: x[0])
for name, cnt in data_sorted:
    percent = round((cnt / tot_cnt) * 100, 4)
    print(f"{name} {percent:.4f}")