directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
n = int(input())
arr = [['#'] * (2 * n + 1) for _ in range(2 * n + 1)]
l, r, u, d = (n, n, n, n)

heading = 0
curr = [n, n]
arr[n][n] = '.'
moves = input()
for move in moves:
    if move == 'L':
        heading = (heading - 1) % 4
    elif move == 'R':
        heading = (heading + 1) % 4
    else:
        curr[0] += directions[heading][0]
        curr[1] += directions[heading][1]
        arr[curr[0]][curr[1]] = '.'
        l = min(l, curr[1])
        r = max(r, curr[1])        
        u = min(u, curr[0])        
        d = max(d, curr[0])        

for i in range(u, d + 1):
    print(*arr[i][l:r + 1], sep='')