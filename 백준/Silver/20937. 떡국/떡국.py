from collections import Counter

n = int(input())
data = list(map(int, input().split()))

data_cnt = Counter(data)
cnt_max = sorted(data_cnt.values(), reverse=True)[0]
print(cnt_max)