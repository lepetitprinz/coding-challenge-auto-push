import sys

input = lambda: sys.stdin.readline().rstrip()

scores = []
for i in range(8):
    scores.append([i + 1, int(input())])
    
scores = sorted(scores, key=lambda x: (-x[1]))
tot_score = 0
problems = []
for p, score in scores[:5]:
    tot_score += score
    problems.append(p)

print(tot_score)
print(*sorted(problems))