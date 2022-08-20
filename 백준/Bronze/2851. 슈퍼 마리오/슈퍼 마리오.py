score = []
for _ in range(10):
    score.append(int(input()))
    
total = 0
idx = 9
for i in range(10):
    total += score[i]
    if total >= 100:
        idx = i
        break

diff_bf = abs(total - score[idx] - 100)
diff_af = abs(total - 100)
if diff_bf == diff_af:
    result = total
elif diff_af < diff_bf:
    result = total
else:
    result = total - score[idx]

print(result)