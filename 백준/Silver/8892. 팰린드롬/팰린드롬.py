from itertools import permutations

def palindrome(string):
    length = len(string)
    
    flag = False
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            break

    else:
        flag = True
        
    return flag
    
t = int(input())
for _ in range(t):
    n = int(input())
    data = [input() for _ in range(n)]
    
    result = None
    for str_1, str_2 in permutations(data, 2):
        string = str_1 + str_2
        if palindrome(string):
            result = string
            break
    else:
        result = 0
        
    print(result)