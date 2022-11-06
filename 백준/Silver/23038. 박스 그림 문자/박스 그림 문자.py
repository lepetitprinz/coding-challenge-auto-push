r, c = map(int, input().split())
pieces = [list(input()) for _ in range(r * 3)]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for i in range(r):
    for j in range(c):
        cr = 3 * i + 1
        cc = 3 * j + 1
        if pieces[cr][cc] == '.':
            pieces[cr][cc] = '#'
            for direction in directions:
                mr = cr + 2 * direction[0]
                mc = cc + 2 * direction[1]
                if mr // 3 < 0 or mr // 3 >= r or mc // 3 < 0 or mc // 3 >= c:
                    continue

                dr = mr - direction[0]
                dc = mc - direction[1]
                pieces[dr][dc] = pieces[mr][mc]

for i in range(r*3):                        
    print(''.join(pieces[i]))