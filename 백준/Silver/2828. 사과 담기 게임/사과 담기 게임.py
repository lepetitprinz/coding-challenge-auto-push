n, m = map(int, input().split())
left = 1
right = m
move_cnt = 0
n_apple = int(input())
for _ in range(n_apple):
    apple = int(input())
    if apple < left:
        diff = left - apple
        move_cnt += diff
        left -= diff
        right -= diff
    elif apple > right:
        diff = apple - right
        move_cnt += diff
        left += diff
        right += diff
        
print(move_cnt)