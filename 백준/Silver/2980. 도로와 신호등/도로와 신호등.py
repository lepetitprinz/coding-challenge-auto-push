import sys
input = lambda: sys.stdin.readline().rstrip()

n, l = map(int, input().split())
sign = {}
for _ in range(n):
    d, r, g = map(int, input().split())
    sign[d] = (r, g)

time = 0
loc = 0
while loc < l:
    loc += 1
    time += 1
    if loc in sign:
        r, g = sign[loc]
        curr = time % (r + g)
        if 0 <= curr < r:
            time += r - curr

print(time)