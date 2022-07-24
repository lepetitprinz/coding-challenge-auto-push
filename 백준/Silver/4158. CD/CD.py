while True:
    n, m = map(int, input().split())
    if (n == 0) & (m == 0) :
        break
    else:
        n_hash = {int(input()): 1 for _ in range(n)}
        result = sum(n_hash.get(int(input()), 0) for _ in range(m))
        print(result)