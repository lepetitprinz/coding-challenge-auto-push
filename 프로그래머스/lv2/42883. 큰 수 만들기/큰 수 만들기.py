def solution(number, k):
    length = len(number)
    n = length - k

    if set(number) == {'9'}:
        answer = '9' * n
    
    answer = ''
    start_idx = 0
    end_idx = length - n
    for i in range(n):
        max_num = '0'
        for num in number[start_idx:end_idx+1]:
            if num > max_num:
                max_num = num
                if max_num == '9':
                    break
        answer += max_num
        start_idx += number[start_idx:].index(max_num) + 1
        end_idx += 1
        
    return answer