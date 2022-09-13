def solution(left, right):
    numbers = list(range(left, right+1))
    
    results = []
    for num in numbers:
        cnt = count_cd(num)
        flag = odd_or_even(cnt)
        results.append(num * flag)       
    
    return sum(results)

def count_cd(number):
    cnt = 0
    for i in range(1, number+1):
        if number % i == 0:
            cnt += 1
    
    return cnt

def odd_or_even(cnt):
    if cnt % 2 == 0:
        return 1
    else:
        return -1