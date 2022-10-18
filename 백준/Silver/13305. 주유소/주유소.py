n = int(input())
distance = list(map(int, input().split()))
oil_list = list(map(int, input().split()))

oil_min = oil_list[0]
price = oil_min * distance[0]
for oil, dist in zip(oil_list[1:-1], distance[1:]):
    if oil < oil_min:
        oil_min = oil
    price += oil_min * dist

print(price)