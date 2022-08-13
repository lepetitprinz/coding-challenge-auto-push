import sys

size_map = {'S': 1, 'M': 2, 'L': 3}

j = int(input())
a = int(input())

j_map = {}
for i in range(j):
    j_map[i+1] = size_map[sys.stdin.readline().rstrip()]

a_map = {}
for _ in range(a):
    size, number = sys.stdin.readline().split()
    if int(number) in a_map:
        a_map[int(number)].append(size_map[size])
    else:
        a_map[int(number)] = [size_map[size]]

cnt = 0
for num, size_list in a_map.items():
    j_size = j_map.get(num, 4)
    if j_size == 4:
        break
    else:
        for s in set(size_list):
            if s <= j_size:
                cnt += 1
                break
print(cnt)