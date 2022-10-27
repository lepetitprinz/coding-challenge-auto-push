n, k = map(int, input().split())
visit = list(map(int, input().split()))

head_idx = 0
cnt = sum(visit[:k])
record = {cnt: 1}
for tail in visit[k:]:
    cnt = cnt - visit[head_idx] + tail
    head_idx += 1
    if cnt in record:
        record[cnt] += 1
    else:
        record[cnt] = 1

result = sorted(record.items(), key=lambda x: x[0], reverse=True)[0]
if result[0] == 0:
    print("SAD")
else:
    print(result[0])
    print(result[1])