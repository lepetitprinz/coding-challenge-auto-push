from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

comb = set(combinations_with_replacement(numbers, m))
for c in sorted(comb):
    print(' '.join(list(map(str, c))))