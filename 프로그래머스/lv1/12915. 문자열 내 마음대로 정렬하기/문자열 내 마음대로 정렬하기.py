def solution(strings, n):
    temp = list()
    for s in strings:
        temp.append(s[n] + s)
    temp.sort()
    answer = [ss[1:] for ss in temp]
    
    return answer