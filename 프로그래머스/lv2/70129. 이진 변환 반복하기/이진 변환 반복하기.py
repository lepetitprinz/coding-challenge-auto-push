def remove_zero(s):
    zero_cnt = s.count('0')
    s_revised = bin(len(s) - zero_cnt)[2:]
    
    return s_revised, zero_cnt

def solution(s):
    revise_cnt = 0
    zero_total_cnt = 0
    while s !='1':
        s, zero_cnt = remove_zero(s)
        revise_cnt += 1
        zero_total_cnt += zero_cnt
    
    return [revise_cnt, zero_total_cnt]