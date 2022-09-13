from itertools import combinations

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True 

def solution(nums):
    cb_list = list(combinations(nums, 3))
    cb_sum = [sum(ls) for ls in cb_list]
    cb_sum = list(cb_sum)
    
    test = [is_prime_num(n) for n in cb_sum]
    
    return sum(test)