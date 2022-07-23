import sys

def get_sign(number):
    sign = 0
    if number > 0:
        sign = '+'
    elif number < 0:
        sign = '-'
    return sign
    
for _ in range(3):
    nums = []
    test = int(sys.stdin.readline())
    for _ in range(test):
        nums.append(int(sys.stdin.readline()))
        
    print(get_sign(sum(nums)))