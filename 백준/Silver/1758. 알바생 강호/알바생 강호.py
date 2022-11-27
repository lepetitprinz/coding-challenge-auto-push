import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
tips = sorted([int(input()) for _ in range(n)], reverse=True)
result = sum(tip - i for i, tip in enumerate(tips) if tip - i > 0)
print(result)