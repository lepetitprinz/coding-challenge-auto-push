default = [1, 1, 2, 2, 2, 8]
nums = list(map(int, input().split()))
diff = [str(d - n) for d, n in zip(default, nums)]

print(' '.join(diff))