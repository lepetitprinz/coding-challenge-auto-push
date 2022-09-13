from math import log

def solution(n,a,b):
    answer = int(log(n, 2))
    
    start_idx = 0
    end_idx = n
    comp_idx = n // 2
    while comp_idx > 1:
        if (a <= comp_idx) and (b <= comp_idx):
            end_idx = comp_idx
            comp_idx = (start_idx + comp_idx) // 2
            answer -= 1
            continue
        elif (a > comp_idx) and (b > comp_idx):
            start_idx = comp_idx
            comp_idx = (comp_idx + end_idx) // 2
            answer -= 1
            continue
        else:
            break

    return answer