def solution(n):
    threes = [3**i for i in range(18, -1, -1)]
    temp = []
    for t in threes:
        if n % t != n:
            temp.append(str(n//t))
            n = n % t
        else:
            temp.append(str(0))
            
    temp = str(int(''.join(temp)))
    temp = temp[::-1]
    
    threes = threes[-1 * len(temp):]
    result = 0
    for a, b in zip(temp, threes):
        result += int(a) * b
            
    return result