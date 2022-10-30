t = int(input())
for _ in range(t):
    n = int(input())
    strings = [input() for _ in range(n)]
    vic = list(range(n))
    for i in range(len(strings[0])):
        if len(vic) == 1:
            print(vic[0]+1)
            break
        cases = set()
        rounds = {}
        for num in vic:
            kind = strings[num][i]
            cases.add(kind)
            if rounds.get(kind, 0):
                rounds[kind].append(num)
            else:
                rounds[kind] = [num]
        
        if cases == {'R','S'}:
            vic = rounds['R']
        elif cases == {'R','P'}:
            vic = rounds['P']
        elif cases == {'S', 'P'}:
            vic = rounds['S']
    else:
        if len(vic) == 1:
            print(vic[0]+1)
        else:
            print(0)