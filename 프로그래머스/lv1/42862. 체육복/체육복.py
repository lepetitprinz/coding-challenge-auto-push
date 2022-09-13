from copy import deepcopy

def solution(n, lost, reserve):
    answer = n - len(lost)
    
    lost.sort()
    reserve.sort()
    
    lost_real = deepcopy(lost)
    reserve_real = deepcopy(reserve)
    
    # Exception
    for res in reserve:
        if res in lost:
            lost_real.remove(res)
            reserve_real.remove(res)
            answer += 1
    
    if len(lost_real) > 0:
        for student in lost_real:
            if (student-1) in reserve_real:
                reserve_real.remove(student - 1)
                answer += 1
                continue
            if (student+1) in reserve_real:
                reserve_real.remove(student + 1)
                answer += 1
                continue
            
    return answer