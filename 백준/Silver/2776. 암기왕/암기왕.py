import sys

t = int(input()) 
for _ in range(t):
    n = int(sys.stdin.readline())
    n_map = {num:1 for num in list(map(int, sys.stdin.readline().split()))}
    m = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().split()))
    result = [n_map.get(i, 0) for i in m_list]
    print(*result, sep='\n')