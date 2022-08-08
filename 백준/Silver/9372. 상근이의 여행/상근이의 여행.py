import sys

test = int(input())
for _ in range(test):
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
    print(n - 1)