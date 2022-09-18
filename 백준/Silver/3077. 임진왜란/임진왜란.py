from itertools import combinations

n = int(input())
total_score = n * (n-1) // 2
data = list(input().split())
seq = {word: i for i, word in enumerate(data)}
answer = list(input().split())

score = 0
for forward, backward in combinations(answer, 2):
    if seq[forward] < seq[backward]:
        score += 1

print(f'{score}/{total_score}')