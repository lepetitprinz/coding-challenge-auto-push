def solution(s):
    ls = s[2:-2].split('},{')
    ls = [list(map(int, l.split(','))) for l in ls]
    ls = [(len(l), l) for l in ls]
    ls = sorted(ls, key=lambda x: x[0])
    
    result = []
    temp = set()
    for l in ls:
        if l[0] == 1:
            result.append(l[1][0])
            temp.add(l[1][0])
        else:
            val = list(set(l[1]) - temp)[0]
            result.append(val)
            temp.add(val)
            
    return result