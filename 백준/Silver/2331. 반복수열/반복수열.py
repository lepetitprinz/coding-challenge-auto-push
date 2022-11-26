def conv_value(num, p):
    str_num = str(num)
    converted_val = sum(int(str_num[i]) ** p for i in range(len(str_num)))
    
    return converted_val

num, p = map(int, input().split())
history = [num]

while True:
    num = conv_value(num, p)
    if num in history:
        result = history.index(num)
        break
    else:
        history.append(num)
        
print(result)