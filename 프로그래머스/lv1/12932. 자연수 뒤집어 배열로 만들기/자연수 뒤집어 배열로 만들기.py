def solution(n):
    length = len(str(n))
    num_list = [int(str(n)[i]) for i in range(length-1, -1, -1)]
    return num_list