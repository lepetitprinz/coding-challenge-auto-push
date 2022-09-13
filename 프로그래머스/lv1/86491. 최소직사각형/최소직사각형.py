def solution(sizes):
    w_max = 0
    h_max = 0
    for w, h in sizes:
        mx = max(w, h)
        mn = min(w, h)
        w_max = max(w_max, mx)
        h_max = max(h_max, mn)
    
    
    answer = w_max * h_max
    return answer