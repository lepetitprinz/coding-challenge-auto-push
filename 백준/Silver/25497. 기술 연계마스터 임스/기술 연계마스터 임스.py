n = int(input())
seq = input()

stack = []
cnt = 0
for s in seq:
    if s in ['L', 'S']:
        stack.append(s)
    elif s == 'R':
        if 'L' in stack:
            stack.remove('L')
            cnt += 1
        else:
            break
    elif s == 'K':
        if 'S' in stack:
            stack.remove('S')
            cnt += 1
        else:
            break
    else:
        cnt += 1

print(cnt)