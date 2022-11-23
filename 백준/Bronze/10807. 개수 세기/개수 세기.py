from collections import Counter
n = int(input())
num_cnt = Counter(list(map(int, input().split())))
print(num_cnt[int(input())])