import sys
from itertools import combinations

vowels = ['a', 'e', 'i', 'o', 'u']

def check(word):
    flag = False
    v_cnt = 0
    c_cnt = 0
    for w in word:
        if w in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    if (v_cnt > 0) & (c_cnt > 1):
        flag = True
    
    return flag
    
l, c = map(int, input().split())
alphabet = sorted(list(sys.stdin.readline().split()))
for word in combinations(alphabet, l):
    if check(word):
        print(''.join(word))