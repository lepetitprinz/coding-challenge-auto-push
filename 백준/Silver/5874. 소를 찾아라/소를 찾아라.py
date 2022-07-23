string = input()
forward = []
backward = []

for i in range(len(string)-1):
    if string[i: i+2] == '((':
        forward.append(i)
    elif string[i: i+2] == '))':
        backward.append(i)

result = 0
b_length = len(backward)
for f in forward:
    for j, b in enumerate(backward):
        if f < b:
            result += b_length - j
            break

print(result)