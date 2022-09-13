def solution(n):
    n_one_cnt = bin(n)[2:].count('1')
    
    add = 1
    while True:
        if bin(n+add)[2:].count('1') == n_one_cnt:
            return n + add
        else:
            add += 1