import sys

n, m = map(int, input().split())
flag = 'Yes'
for _ in range(m):
    cnt = int(sys.stdin.readline())
    stack = list(map(int, sys.stdin.readline().split()))
    if stack != sorted(stack, reverse=True):
        flag = 'No'
        break

print(flag)