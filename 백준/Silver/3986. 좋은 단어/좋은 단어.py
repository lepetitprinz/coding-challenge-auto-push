def check(string):
    flag = False
    if len(string) % 2 == 0:
        stack = [string[0]]
        for s in string[1:]:
            if len(stack) == 0:
                stack.append(s)
            else:
                if s == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s)
        if len(stack) == 0:
            flag = True
    
    return flag

test = int(input())
result = 0
for _ in range(test):
    string = input()
    result += check(string)
    
print(result)