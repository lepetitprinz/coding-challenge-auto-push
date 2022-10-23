from itertools import combinations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
cases = combinations(nums, m)
for case in cases:
    print(*case)