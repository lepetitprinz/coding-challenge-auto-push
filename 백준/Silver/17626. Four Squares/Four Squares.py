def solution(n):
    result = 4
    sqrt_n = n ** 0.5
    if sqrt_n == int(sqrt_n):
        return 1
    else:
        max_val = int(sqrt_n)
        for i in range(max_val, 0, -1):
            for j in range(1, max_val + 1):
                value = i ** 2 + j ** 2
                if value == n:
                    return 2
                elif value > n:
                    break
                    
        for i in range(max_val, 0, -1):
            for j in range(1, max_val + 1):
                for k in range(1, max_val + 1):
                    value = i ** 2 + j ** 2 + k ** 2
                    if value == n:
                        return 3
                    elif value > n:
                        break
        
    return result

n = int(input())
result = solution(n)
print(result)