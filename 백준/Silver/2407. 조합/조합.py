def factorial(x):
    result = 1
    for i in range(2, x+1):
        result *= i
        
    return result

n, m = map(int, input().split())
print(factorial(n) // factorial(m) // factorial(n-m))