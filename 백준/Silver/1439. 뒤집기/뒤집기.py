seq = input()
cnt = [0, 0]
temp = int(seq[0])
cnt[temp] = 1
for s in seq[1:]:
    if int(s) != temp:
        cnt[int(s)] += 1
        temp = int(s)

print(min(cnt))