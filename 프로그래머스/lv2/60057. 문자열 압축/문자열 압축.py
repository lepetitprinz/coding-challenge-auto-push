def solution(s):
    if len(s) == 1:
        result = 1
    else:
        split_list = split_string(s)
        results = [len(compress(str_list)) for str_list in split_list]
        result = min(results)

    return result

def split_string(s):
    split_list = []
    for i in range(1, (len(s)//2) + 1):
        chunk = [s[j: j+i] for j in range(0, len(s), i)]
        split_list.append(chunk)
    
    return split_list

def compress(str_list):
    length = len(str_list)
    string = ''
    cnt = 1
    for i in range(length-1):
        if str_list[i+1] == str_list[i]:
            cnt += 1
            if i == length-2:
                string = string + str(cnt) + str_list[i]
        else:
            if cnt != 1:
                string = string + str(cnt) + str_list[i]
                cnt = 1
            else:
                string = string + str_list[i]
            if i == length-2:
                string = string + str_list[i+1]
    
    return string