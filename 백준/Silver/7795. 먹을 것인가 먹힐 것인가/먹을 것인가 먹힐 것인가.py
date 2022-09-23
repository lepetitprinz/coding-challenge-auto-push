import sys

input = lambda: sys.stdin.readline().rstrip()

test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    n_list = sorted(list(map(int, input().split())), reverse=True)
    m_list = sorted(list(map(int, input().split())), reverse=True)
    
    count = 0
    for a in n_list:
        for i, b in enumerate(m_list):
            if a > b:
                count += m - i 
                break
    print(count)