r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

words = []
for i in range(r):
    temp = []
    for j in range(c):
        char = arr[i][j]
        if char != '#':
            temp.append(char)
        else:
            if len(temp) > 1:
                words.append(''.join(temp))
            temp = []
    if len(temp) > 1:
        words.append(''.join(temp))

for i in range(c):
    temp = []
    for j in range(r):
        char = arr[j][i]
        if char != '#':
            temp.append(char)
        else:
            if len(temp) > 1:
                words.append(''.join(temp))
            temp = []
    if len(temp) > 1:
        words.append(''.join(temp))

words = sorted(words)
print(words[0])