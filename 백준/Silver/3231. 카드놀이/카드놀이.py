import sys

n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0
i = 1
idx = nums.index(i)
while i < n:
    i += 1
    temp = nums.index(i)
    if temp < idx:
        cnt += 1
    idx = temp

print(cnt)