import math

def solution(w,h):
    answer = 0
    if (w == 1) or (h == 1):
        answer = 0
        
    else:
        tot_cnt = w * h
        gcd = math.gcd(w, h)
        w_min = w // gcd
        h_min = h // gcd

        cnt = 0
        rate = h_min / w_min
        for i in range(w_min):
            left = math.floor(rate * i)
            right = math.ceil(rate * (i+1))
            cnt += right - left
        
        answer = tot_cnt - gcd * cnt
    
    return answer