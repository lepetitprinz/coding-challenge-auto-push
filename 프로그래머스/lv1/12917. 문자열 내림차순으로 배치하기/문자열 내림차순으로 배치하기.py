def solution(s):
    upper_list = [element for element in s if element.isupper()]
    lower_list = [element for element in s if element.islower()]
    lower_list = sorted(lower_list, reverse=True)
    upper_list = sorted(upper_list, reverse=True)
    
    answer = ''.join(lower_list + upper_list)
    return answer