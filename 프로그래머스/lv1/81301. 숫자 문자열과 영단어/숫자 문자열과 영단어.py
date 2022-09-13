def solution(s):
    alpha_map = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    for num_str in alpha_map:
        if num_str in s:
            s = s.replace(num_str, alpha_map[num_str])
    
    answer = int(s)
    
    return answer