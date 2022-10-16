from itertools import combinations
from collections import Counter

str_a = list(input())
str_b = list(input())
str_c = list(input())
k = int(input())

comb = []
for string in [str_a, str_b, str_c]:
    comb.extend(list(combinations(string, k)))

result = []
for key, val in Counter(comb).items():
    if val >= 2:
        result.append(''.join(key))

if len(result) == 0:
    print(-1)
else:
    result = sorted(result)
    print(*result, sep='\n')