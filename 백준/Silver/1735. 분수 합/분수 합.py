from math import gcd

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

d = d1 * d2
n = n1 * d2 + n2 * d1
g = gcd(n, d)

print(f"{n//g} {d//g}")