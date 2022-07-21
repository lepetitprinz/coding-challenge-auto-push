case = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 & p == 0 & v == 0:
        break
    else:
        result = v // p * l + min(l, v % p)
        print(f'Case {case}: {result}')
        case += 1