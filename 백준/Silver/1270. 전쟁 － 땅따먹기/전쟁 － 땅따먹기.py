import sys

def count_people(people, length):
    count = {}
    for p in people:
        if p not in count:
            count[p] = 1
        else:
            count[p] += 1

    most = sorted(count.items(), key=lambda x: x[1], reverse=True)[0]
    
    result = 'SYJKGW'
    if most[1] > (length/2):
        result = most[0]
    
    return result

n = int(input())
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    k, people = data[0], data[1:]
    result = count_people(people, k)
    print(result)