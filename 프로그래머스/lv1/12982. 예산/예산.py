def solution(d, budget):
    cnt = 0
    d = sorted(d)
    for price in d:
        if budget - price >=0:
            budget -= price
            cnt += 1
        else:
            break
    
    return cnt