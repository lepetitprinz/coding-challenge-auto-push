def backtrack(data, result, m):
    temp = []
    while m > 0:
        for r in result:
            for d in data:
                if d >= r[-1]:
                    add = r + [d]
                    if add not in temp:
                        temp.append(add)
        temp = sorted(temp)
        result = backtrack(data, temp, m - 1)
        return result

    return result


n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = [[i] for i in data]
result = backtrack(data, result, m - 1)
for r in result:
    print(*r)