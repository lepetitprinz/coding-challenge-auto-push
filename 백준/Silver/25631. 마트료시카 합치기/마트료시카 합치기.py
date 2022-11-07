from collections import Counter

n = int(input())
data = list(map(int, input().split()))

cnt = Counter(data)
max_cnt = max(cnt.values())
print(max_cnt)