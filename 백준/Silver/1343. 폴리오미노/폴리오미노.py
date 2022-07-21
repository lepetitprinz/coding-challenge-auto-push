def split_string(string):
    split = []
    temp = string[0]
    for s in string[1:]:
        if s == temp[-1]:
            temp += s
        else:
            split.append(temp)
            temp = s
    split.append(temp)
    
    return split

def poliomino(word):
    result = None
    
    length = len(word)
    div = length// 4
    mod = length % 4
    
    if mod in [0, 2]:
        result = 'AAAA' * div + 'BB' * (mod // 2)

    return result    
        
string = input()
split = split_string(string)
result = ''
for s in split:
    if '.' in s:
        result += s
    else:
        poli = poliomino(s)
        if poli is not None:
            result += poli
        else:
            result = -1
            break

print(result)