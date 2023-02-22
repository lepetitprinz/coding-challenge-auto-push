import sys

input = lambda: sys.stdin.readline().rstrip()

def binary_search(loc, n, c):
    left = 1
    right = loc[-1] - loc[0] + 1
    
    while left < right:
        mid = (left + right) // 2
        if is_installable(loc, mid) < c:
            right = mid
        else:
            left = mid + 1
    
    return left - 1
    
def is_installable(loc, distance):
    cnt = 1
    last_loc = loc[0]
    
    for l in loc:
        if l - last_loc >= distance:
            cnt += 1
            last_loc = l
    
    return cnt
    
n, c = map(int, input().split())
loc = sorted([int(input()) for _ in range(n)])
ans = binary_search(loc, n, c)
print(ans)