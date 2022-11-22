def dp(n):
    if n in [1, 2]:
        curr = 3 if n == 1 else 7
    else:
        prev_2 = 3
        prev_1 = 7
        curr = 0
        for _ in range(n - 2):
            curr = 2 * prev_1 + prev_2
            curr = curr % 9901
            prev_2, prev_1 = prev_1, curr
    
    return curr % 9901
    
n = int(input())
result = dp(n)
print(result)