def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(3, total+1):
        if (total % i == 0) and (i - 2) * (total//i - 2) == yellow:
            answer = [total//i, i]
            break
            
    return answer