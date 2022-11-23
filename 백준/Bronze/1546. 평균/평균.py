n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
scores_new = [(score/max_score)*100 for score in scores]
scores_new_avg = sum(scores_new)/n
print(scores_new_avg)