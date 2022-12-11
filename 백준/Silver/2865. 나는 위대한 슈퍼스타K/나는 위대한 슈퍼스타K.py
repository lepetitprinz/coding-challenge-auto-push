import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())

scores = {}
for i in range(m):
    data = list(input().split())
    for j in range(n):
        p = int(data[j * 2])
        score = float(data[j * 2 + 1])
        if i == 0:
            scores[p] = [score]
        else:
            scores[p].append(score)

max_scores = []
for p, score in scores.items():
    max_scores.append(max(score))
    
result = sum(sorted(max_scores, reverse=True)[:k])
print(round(result, 1))