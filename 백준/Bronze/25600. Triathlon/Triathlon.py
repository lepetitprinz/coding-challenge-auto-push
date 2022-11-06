n = int(input())
score = 0
for _ in range(n):
    a, d, g = map(int, input().split())
    if a == d+g:
        score = max(score,2*(a**2))
    else:
        score = max(score,a * (d+g))
        
print(score)