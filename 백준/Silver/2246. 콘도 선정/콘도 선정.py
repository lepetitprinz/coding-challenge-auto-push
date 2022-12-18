import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = {}
dist_list = []
for _ in range(n):
    d, c = map(int, input().split())
    if d in data:
        data[d].append(c)
    else:
        data[d] = [c]
        dist_list.append(d)
        
dist_list = sorted(dist_list, reverse=True)
for k, v in data.items():
    data[k] = sorted(v)

cnt = 1
for i, dist in enumerate(dist_list[:-1]):
    cost = data[dist][0]
    for comp_dist in dist_list[i + 1:]:
        comp_cost = data[comp_dist][0]
        if comp_cost <= cost:
            break
    else:
        cnt += 1

print(cnt)