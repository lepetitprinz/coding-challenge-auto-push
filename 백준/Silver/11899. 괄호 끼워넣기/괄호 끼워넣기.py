string = input()
stack = [string[0]]

for s in string[1:]:
    if len(stack) == 0:
        stack.append(s)
    else:
        if (stack[-1] == '(') & (s == ')'):
            stack.pop()
        else:
            stack.append(s)

print(len(stack))