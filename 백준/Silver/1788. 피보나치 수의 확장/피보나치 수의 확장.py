def dp(n, sign):
    result = 0
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        prev2 = 0
        prev1 = 1
        for i in range(n - 1):
            result = (prev2 + prev1) % int(1e9)
            prev1, prev2 = result, prev1
    
    if sign == 'minus':
        if n % 2 == 0:
            s = -1
        else:
            s = 1
    elif sign == 'plus':
        s = 1
    else:
        s = 0
    
    return result % int(1e9), s

n = int(input())

sign = None
if n > 0:
    sign = 'plus'
elif n < 0:
    sign = 'minus'
else:
    sign = 'zero'
    
result, sign = dp(abs(n), sign)
print(sign)
print(result)