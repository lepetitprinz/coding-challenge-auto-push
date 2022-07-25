n = list(map(int, list(input())))
if 0 not in n:
    print(-1)
else:
    if sum(n) % 3 == 0:
        result = sorted(n, reverse=True)
        print(*result, sep='')
    else:
        print(-1)