n = int(input())
for _ in range(n):
    lt, wt, le, we = map(int, input().split())
    area_t = lt * wt
    area_e = le * we
    if area_t > area_e:
        print("TelecomParisTech")
    elif area_t < area_e:
        print("Eurecom")
    else:
        print("Tie")