import sys

input = lambda: sys.stdin.readline().rstrip()

def stack(values):
    cnt = 0
    stack = [0]
    for val in values[1:]:
        if stack:
            prev = stack[-1]
            if val > prev:
                stack.append(val)
                cnt += 1
            elif val == prev:
                continue
            else:
                while stack:
                    if stack[-1] > val:
                        stack.pop()
                    elif stack[-1] == val:
                        break
                    else:
                        stack.append(val)
                        cnt += 1
                        break
        else:
            stack.append(val)
            if val > 0:
                cnt += 1

    return cnt


t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    t = data[0]
    values = data[1:]
    result = stack(values)
    print(t, result)