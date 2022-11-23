n, x = map(int, input().split())
nums = list(map(int, input().split()))
nums_over = [str(num) for num in nums if num < x]
print(' '.join(nums_over))