stick = input()
result = 0
stack = []
for i in range(len(stick)):
    if stick[i] == '(':
        stack.append(stick[i])
    else:
        if stick[i-1] == '(': 
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)