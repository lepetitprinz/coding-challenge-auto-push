import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

def search_loc(arr):
    houses = []
    chickens = []

    for i, row in enumerate(arr):
        for j, val in enumerate(row):
            if val == 1:
                houses.append((i, j))
            elif val == 2:
                chickens.append((i, j))

    return houses, chickens


def calc_dist(p1, p2):
    r1, c1 = p1
    r2, c2 = p2

    return abs(r1 - r2) + abs(c1 - c2)


def get_distance_by_house(houses, chickens):
    distances = []
    for house in houses:
        distance = {}
        for i, chicken in enumerate(chickens):
            distance[i] = calc_dist(house, chicken)
        distances.append(distance)

    return distances


def get_min_distance(distances, c, m):
    candidates = list(combinations(range(c), m))
    city_distances = []
    for candidate in candidates:
        city_distance = 0
        for house in distances:
            house_min_dist = min(house[i] for i in candidate)
            city_distance += house_min_dist

        city_distances.append(city_distance)

    return min(city_distances)


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

houses, chickens = search_loc(arr)
distances = get_distance_by_house(houses, chickens)
result = get_min_distance(distances, len(chickens), m)
print(result)