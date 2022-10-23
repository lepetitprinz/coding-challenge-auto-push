def backtrack(data, m, step, result):
    while step < m:
        upper = []
        for v in result:
            lower = []
            for add in data:
                if add >= v[-1]:
                    lower.append(v + [add])
            upper.extend(lower)
        result = upper
        result = backtrack(data, m, step + 1, result)
        return result
    return result


n, m = map(int, input().split())
data = set(map(int, input().split()))
data = sorted(list(data))

result = [[v] for v in data]
result = backtrack(data, m, 1, result)
for row in result:
    print(*row)