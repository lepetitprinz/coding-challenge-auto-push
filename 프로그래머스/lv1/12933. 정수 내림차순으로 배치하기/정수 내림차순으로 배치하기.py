def solution(n):
    n_list = list(str(n))
    n_list = [int(n) for n in n_list]
    
    n_list = sorted(n_list, reverse=True)
    n_list = [str(n) for n in n_list]
    result = ''.join(n_list)
    return int(result)