def door(n):
    room = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1 , i):
            if room[j]:
                room[j] = 0
            else:
                room[j] = 1
    
    return sum(room)

t = int(input())
for _ in range(t):
    n = int(input())
    print(door(n))