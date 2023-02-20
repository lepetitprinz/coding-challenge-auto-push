def tree(start, end, depth):
    if start == end:
        level[depth].append(data[start])
        return

    root = (start + end) // 2
    level[depth].append(data[root])
    tree(start, root - 1, depth + 1)
    tree(root + 1, end, depth + 1)

k = int(input())
data = list(map(int, input().split()))
level = [[] for _ in range(k)]
        
tree(start=0, end=len(data)-1, depth=0)
for row in level:
    print(*row)