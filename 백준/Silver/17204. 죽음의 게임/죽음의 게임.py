n, k = map(int, input().split())

direction = {}
for i in range(n):
    direction[i] = int(input())

count = 0
loc = 0
while count < n:
    count += 1
    loc = direction[loc]
    if loc == k:
        break

if count != n:
    print(count)
else:
    print(-1)