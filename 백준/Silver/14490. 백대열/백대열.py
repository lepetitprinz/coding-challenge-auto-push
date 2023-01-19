from math import gcd

a, b = input().split(":")
a = int(a)
b = int(b)
g = gcd(a, b)

result = print(f"{a//g}:{b//g}")