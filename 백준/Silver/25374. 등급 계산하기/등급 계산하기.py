n = int(input())
scores = sorted(list(map(int, input().split())), reverse=True)
grades = [0.04, 0.11, 0.23, 0.4, 0.6, 0.77, 0.89, 0.96]

result = [0] * 9
prev = scores[0]
rank = 0

for i, score in enumerate(scores):
    if score == prev:
        result[rank] += 1
    else:
        rate = (i + 1) / n
        if rate <= grades[0]:
            result[0] += 1
            rank = 0
        elif rate <= grades[1]:
            result[1] += 1
            rank = 1
        elif rate <= grades[2]:
            result[2] += 1
            rank = 2
        elif rate <= grades[3]:
            result[3] += 1
            rank = 3
        elif rate <= grades[4]:
            result[4] += 1
            rank = 4
        elif rate <= grades[5]:
            result[5] += 1
            rank = 5
        elif rate <= grades[6]:
            result[6] += 1
            rank = 6
        elif rate <= grades[7]:
            result[7] += 1
            rank = 7
        else:
            result[8] += 1
            rank = 8
    prev = score
print(*result, sep='\n')