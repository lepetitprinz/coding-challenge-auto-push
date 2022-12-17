t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = int(''.join(input().split()))
    y = int(''.join(input().split()))    
    board = input().split()
    board = board + board[:m - 1]
    
    cnt = 0
    for i in range(n):
        num = int(''.join(board[i: i + m]))
        if x <= num <= y:
            cnt += 1
            
    print(cnt)