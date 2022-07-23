import sys

n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums = nums[::-1]
max_height = 0
cnt = 0
for num in nums:
    if num > max_height:
        cnt += 1
        max_height = num

print(cnt)