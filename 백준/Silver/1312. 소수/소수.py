a, b, n = map(int, input().split())

a %= b
for _ in range(n):
    q, a = divmod(a * 10, b)
    
print(q)