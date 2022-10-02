def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        result = result % 10
    
    return result
        
n = int(input())
print(factorial(n))