n = int(input())
market = list(map(int, input().split()))
seq = [0, 1, 2]
cnt = 0
idx = 0
for m in market:
    if m == seq[idx]:
        cnt += 1
        idx = idx + 1 if idx < 2 else 0

print(cnt)