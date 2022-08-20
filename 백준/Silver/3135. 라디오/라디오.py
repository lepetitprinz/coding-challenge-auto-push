import sys

a, b = map(int, input().split())
n = int(input())
bookmarks = [int(sys.stdin.readline()) for _ in range(n)]

diff1 = abs(b - a)
diff2 = min([abs(b - bookmark) for bookmark in bookmarks]) + 1
print(min(diff1, diff2))