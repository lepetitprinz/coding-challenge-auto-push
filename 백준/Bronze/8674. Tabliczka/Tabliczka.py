a, b = map(int, input().split())

result = min(a, b) 
if a % 2 == 0 or b % 2 == 0:
    result = 0
print(result)