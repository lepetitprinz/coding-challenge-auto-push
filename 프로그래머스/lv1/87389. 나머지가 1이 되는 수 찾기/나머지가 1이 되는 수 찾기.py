def solution(n):
    mod_list = []
    for i in range(2, n):
        if n % i == 1:
            mod_list.append(i)
    
    return min(mod_list)