def solution(s):
    str_list = list(s)

    stack = [str_list[0]]
    for string in str_list[1:]:
        if len(stack) == 0:
            stack.append(string)
        else:
            if stack[-1] == string:
                stack.pop()
            else:
                stack.append(string)

    if stack:
        answer = 0
    else:
        answer = 1

    return answer