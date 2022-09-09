x, y = map(int, input().split())

count = 0
first = max(x, y)
last = min(x, y)
count += first
count += last
count += last // 10

print(count)