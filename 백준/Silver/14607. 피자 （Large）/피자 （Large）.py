def dp(n):
    temp = 0
    if n > 1:
        for i in range(1, n):
            temp += i
            
    return temp

n = int(input())

result = dp(n)
print(result)