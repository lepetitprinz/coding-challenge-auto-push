n, x = map(int, input().split())
nums = list(map(int, input().split()))
nums_over = (num for num in nums if num < x)
print(*nums_over)