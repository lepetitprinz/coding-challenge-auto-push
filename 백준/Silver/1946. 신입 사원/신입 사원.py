import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(data):
    bf_x, bf_y = data[0]
    cnt = 1
    for x, y in data[1:]:
        if x > bf_x and y < bf_y:
            cnt += 1
            bf_x = x
            bf_y = y

    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    for _ in range(n):
        x, y = map(int, input().split())
        data.append([x, y])

    data = sorted(data, key=lambda x: (x[0], -x[1]))
    result = solve(data)
    print(result)