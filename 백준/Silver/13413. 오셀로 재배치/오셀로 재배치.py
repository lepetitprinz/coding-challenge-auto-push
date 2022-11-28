import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(seq_1, seq_2):
    seq_1_b = 0
    seq_2_b = 0
    not_match = 0
    for v1, v2 in zip(seq_1, seq_2):
        if v1 == 'B':
            seq_1_b += 1
        if v2 == 'B':
            seq_2_b += 1
        if v1 != v2:
            not_match += 1
    
    diff = abs(seq_1_b - seq_2_b)
    
    return diff + (not_match - diff) // 2


t = int(input())
for _ in range(t):
    n = int(input())
    seq_1 = list(input())
    seq_2 = list(input())
    result = solve(seq_1, seq_2)
    print(result)