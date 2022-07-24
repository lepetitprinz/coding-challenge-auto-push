from math import ceil

n, m = map(int, input().split())
min_set = 1000
min_each = 1000

for _ in range(m):
    s, e = map(int, input().split())
    if s < min_set:
        min_set = s
    if e < min_each:
        min_each = e

each_price = n * min_each
set_price = ceil(n / 6) * min_set
multi_price = (n // 6) * min_set + (n % 6) * min_each

print(min(each_price, set_price, multi_price))