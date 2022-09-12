import sys

def calc_distance(points):
    distance = 0
    for i in range(len(points) - 1):
        distance += manhatten_distance(points[i], points[i + 1])

    return distance


def manhatten_distance(start, end):
    x_s, y_s = start
    x_e, y_e = end

    return abs(x_e - x_s) + abs(y_e - y_s)


n = int(input())
x_s, y_s, x_e, y_e = map(int, sys.stdin.readline().split())

results = []
for i in range(1, n + 1):
    points = [[x_s, y_s]]
    for _ in range(int(sys.stdin.readline())):
        points.append(list(map(int, sys.stdin.readline().split())))
    points.append([x_e, y_e])
    distance = calc_distance(points)
    results.append([i, distance])

best = sorted(results, key=lambda x: x[1])[0]
print(best[0])