from collections import deque

def bfs(start, end):
    queue = deque([[start, 0]])
    visited = set([start])
    
    method = 0
    min_cnt = 10 ** 5
    flag = False
    while queue:
        loc, cnt = queue.popleft()
        visited.add(loc)
        
        if flag and cnt > min_cnt:
            continue
                
        if loc == end:
            if not flag:
                min_cnt = cnt
                method += 1
                flag = True
            else:
                method += 1
        
        for new_loc in [loc + 1, loc - 1 , loc * 2]:
            if 0 <= new_loc <= 10 ** 5 and new_loc not in visited:
                queue.append([new_loc, cnt + 1])
                
    return (min_cnt, method)
    
start, end = map(int, input().split())
result = bfs(start, end)
print(*result, sep='\n')