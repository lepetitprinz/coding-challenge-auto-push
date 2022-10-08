import sys

input = lambda: sys.stdin.readline().rstrip()

def make_data(n):
    pair = []
    cost = []
    half_cost = []
    for _ in range(n):
        p, s = map(int, input().split())
        pair.append((p, s))
        cost.append(p + s)
        half_cost.append(p / 2 + s)

    return pair, cost, half_cost


def min_cost_pair(pair, cost, half_cost):
    min_cost_pair = None
    min_cost = 0
    for (p, s), c, half_c in zip(pair, cost, half_cost):
        diff = half_c - c
        if diff < min_cost:
            min_cost = diff
            min_cost_pair = (p, s)

    return min_cost_pair


def cnt_max_present(pair, min_pair, b):
    pair.remove(min_pair)
    pair = sorted(pair, key=lambda x: x[0] + x[1])

    cnt = 0
    flag = False
    for p, s in pair:
        c = p + s
        if c <= b:
            b -= c
            cnt += 1
        else:
            half_c = p / 2 + s
            if half_c <= b:
                b -= half_c
                cnt += 1
                flag = True

    if not flag:
        p, s = min_pair
        if p / 2 + s <= b:
            cnt += 1

    return cnt


n, b = map(int, input().split())
pair, cost, half_cost = make_data(n)
min_pair = min_cost_pair(pair, cost, half_cost)
result = cnt_max_present(pair, min_pair, b)
print(result)