from itertools import product

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
cases = product(nums, repeat=m)
for case in cases:
    print(*case)