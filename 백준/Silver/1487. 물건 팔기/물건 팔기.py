import sys
n = int(input())

data = {}
for _ in range(n):
    price, package = map(int, sys.stdin.readline().split())
    if price in data:
        data[price].append(package)
    else:
        data[price] = [package]

data = sorted(data.items(), key=lambda x: x[0], reverse=True)

pack_list = []
count = 0
results = []
for price, packages in data:
    pack_list.extend(packages)
    choose = []
    for package in pack_list:
        if package < price:
            choose.append(package)

    profit = price * len(choose) - sum(choose)
    results.append([price, profit])

result = sorted(results, key=lambda x: (-x[1], x[0]))[0]
if result[1] > 0:
    print(result[0])
else:
    print(0)