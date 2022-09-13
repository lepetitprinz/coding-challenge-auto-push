def solution(x):
    num_list = [int(num) for num in str(x)]
    num_sum = sum(num_list)
    
    answer = False
    if x % num_sum == 0:
        answer = True
    
    return answer