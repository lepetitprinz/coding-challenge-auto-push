cnt_map = {'(': 1, ')': -1}

def solution(s):
    flag = True
    status = 0
    for bracket in s:
        status += cnt_map[bracket]
        if status < 0:
            flag = False
            break
    
    if status != 0:
        flag = False
    
    return flag