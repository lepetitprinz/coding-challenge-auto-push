string = input()
result = ''
temp = ''
flag = True
for s in string:
    if (s == ' ') & flag:
        result += temp[::-1]
        result += ' '
        temp = ''
    elif s == '<':
        result += temp[::-1]
        temp = s
        flag = False
    elif s == '>':
        result = result + temp + s
        temp = ''
        flag = True
    else:
        temp += s
if flag:
    result += temp[::-1]
else:
    result += temp
        
print(result)