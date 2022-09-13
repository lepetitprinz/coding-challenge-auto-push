import math
from itertools import permutations
    
def solution(numbers):
    numbers = list(numbers)
    num_list = make_num_list(numbers)
    prime_list = [is_prime(num) for num in num_list]
    
    return sum(prime_list)
    
def make_num_list(numbers):
    num_list = []
    for i in range(1, len(numbers)+1):
        num_list.extend(list(permutations(numbers, i)))
    num_list = [int(''.join(num)) for num in num_list]
    
    return list(set(num_list))

def is_prime(x):
    if (x == 0) or (x == 1):
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True