import sys

scenario = 0
while True:
    scenario += 1
    n = int(sys.stdin.readline())
    if n == 0:
        break
    name = {i+1: sys.stdin.readline().rstrip() for i in range(n)}
    entry = []
    for _ in range(2 * n - 1):
        person, val = sys.stdin.readline().split()
        person = int(person)
        if person in entry:
            entry.remove(person)
        else:
            entry.append(person)
    
    print(scenario, name[entry[0]])