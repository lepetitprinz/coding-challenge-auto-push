import sys

n = int(input())
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    result = 'NOT anagrams'
    if sorted(a) == sorted(b):
        result = 'anagrams'
    print(f'{a} & {b} are {result}.')