import sys
n, m = map(int, input().split())

address_map = {}
for _ in range(n):
    site, pw = sys.stdin.readline().split()
    address_map[site] = pw

for _ in range(m):
    s = sys.stdin.readline().rstrip()
    print(address_map[s])