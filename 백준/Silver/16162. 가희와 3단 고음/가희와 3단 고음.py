n, a, d = map(int, input().split())
data = list(map(int, input().split()))

count = 0
curr = a
for i in data:
    if i == curr:
        count += 1
        curr += d
print(count)