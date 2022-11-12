import sys

input = lambda : sys.stdin.readline().rstrip()

def solve(a, b, c):
    sum_set = set()
    for i in a:
        for j in b:
            for k in c:
                sum_set.add(str(i + j + k))
    cnt = 0
    check = set(['5', '8'])
    for val in sum_set:
        vals = set(val)
        if vals.issubset(check):
            cnt += 1

    return cnt

t = int(input())
for _ in range(t):
    n_a = int(input())
    a = set(map(int, input().split()))
    n_b = int(input())
    b = set(map(int, input().split()))
    n_c = int(input())
    c = set(map(int, input().split()))

    result = solve(a, b, c)
    print(result)