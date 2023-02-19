from math import ceil

r, c, n = map(int, input().split())
r_n = int(ceil(r / n))
c_n = int(ceil(c / n))
print(r_n * c_n)
