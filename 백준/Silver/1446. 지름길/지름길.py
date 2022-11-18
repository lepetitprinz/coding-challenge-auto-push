import sys

input = lambda: sys.stdin.readline().rstrip()

def get_path(n, dist):
    path = {}
    for _ in range(n):
        f, t, l = map(int, input().split())
        if t <= dist:
            if t in path:
                path[t].append((f, l))
            else:
                path[t] = [(f, l)]

    return path


def dp(dist, path):
    d = [0] * (dist + 1)
    for i in range(1, dist + 1):
        if i in path:
            route = [d[i - 1] + 1]
            for f, length in path[i]:
                route.append(d[f] + length)
            d[i] = min(route)
        else:
            d[i] = d[i - 1] + 1

    return d[dist]


n, dist = map(int, input().split())
path = get_path(n, dist)
result = dp(dist, path)

print(result)