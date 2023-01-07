chmeical = {"H": 1, "C": 12, "O": 16}
stack = []

for i in input():
    if i == "(":
        stack.append(i)
    elif i == ")":
        check = 0

        while True:
            target = stack.pop()
            if target == "(":
                break

            check += target

        stack.append(check)

    elif i in chmeical:
        stack.append(chmeical[i])

    else:
        stack[-1] *= int(i)

print(sum(stack))