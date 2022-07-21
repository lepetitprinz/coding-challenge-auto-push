cases = [
    # ㅣ
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],
    # ㄱㄴ
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,0),(1,0),(1,-1),(2,-1)],
    # ㄱ
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(2,0),(2,-1)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(0, -1),(1,-1),(2,-1)],
    # ㅓ
    [(0,0),(1,0),(1, -1),(2,0)],
    [(0,0),(0,1),(-1,1),(0,2)],
    [(0,0),(1,0),(1,1),(2,0)],
    [(0,0),(0,1),(1,1),(0,2)],
    # ㅁ
    [(0,0),(1,0),(0,1),(1,1)]
]

t = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(n)]
        result = -4000000
        for i in range(n):
            for j in range(n):
                for case in cases:
                    temp = 0
                    end = True
                    for c in case:
                        x, y = c
                        x, y = x+i, y+j
                        if x < 0 or x > n-1 or y < 0 or y > n-1:
                            end = False
                            break
                        temp += arr[x][y]
                    if end and temp > result:
                        result = temp
        print(f'{t}. {result}')
        t += 1