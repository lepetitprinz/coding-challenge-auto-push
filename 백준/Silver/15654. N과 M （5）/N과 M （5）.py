from itertools import permutations

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))

sequences = permutations(data, m)
for sequence in sequences:
    print(*sequence)