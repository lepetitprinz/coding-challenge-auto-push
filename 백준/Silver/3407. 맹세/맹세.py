from collections import deque

element = set([
    'h','he','li','be','b','c','n','o','f','ne','na','mg',
    'al','si','p','s','cl','ar','k','ca','sc','ti','v','cr',
    'mn','fe','co','ni','cu','zn','ga','ge','as','se','br','kr',
    'rb','sr','y','zr','nb','mo','tc','ru','rh','pd','ag','cd',
    'in','sn','sb','te','i','xe','cs','ba','hf','ta','w','re',
    'os','ir','pt','au','hg','tl','pb','bi','po','at','rn','fr',
    'ra','rf','db','sg','bh','hs','mt','ds','rg','cn','fl',
    'lv','la','ce','pr','nd','pm','sm','eu','gd','tb','dy',
    'ho','er','tm','yb','lu','ac','th','pa','u','np','pu','am',
    'cm','bk','cf','es','fm','md','no','lr'
])

def check(word):
    queue = deque()
    queue.append(word)
    while queue:
        w = queue.popleft()
        if w == '':
            break
        for i in range(2):
            if len(w) > i:
                if w[0:i+1] in element:
                    temp = w[i+1:]
                    if temp not in queue:
                        queue.append(temp)

    if w == '':
        result = 'YES'
    else:
        result = 'NO'

    return result
                    
n = int(input())
for _ in range(n):
    word = input()
    result = check(word)
    print(result)