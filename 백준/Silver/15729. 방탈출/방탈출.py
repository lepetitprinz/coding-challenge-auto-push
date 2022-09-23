n = int(input())
data = [0] * n
goal = list(map(int, input().split()))

count = 0
for i in range(n):
    if goal[i] == 1 and data[i] == 0:
        count += 1
        for j in range(i, i + 3):
            if j < n:
                if data[j] == 0:
                    data[j] = 1
                else:
                    data[j] = 0
    elif goal[i] == 0 and data[i] == 1:
        count += 1
        for j in range(i, i + 3):
            if j < n:
                if data[j] == 0:
                    data[j] = 1
                else:
                    data[j] = 0

print(count)