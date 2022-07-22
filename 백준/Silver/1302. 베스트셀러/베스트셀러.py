n = int(input())
cnt = {}

for _ in range(n):
    book = input()
    if book in cnt:
        cnt[book] += 1
    else:
        cnt[book] = 1
        
bestseller = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[0][0]
print(bestseller)