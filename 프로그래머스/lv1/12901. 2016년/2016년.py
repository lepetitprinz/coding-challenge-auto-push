def solution(a, b):
    name = {'0': "FRI", '1': "SAT", '2': "SUN", '3': "MON", '4': "TUE", '5': "WED", '6': "THU"}
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    days = sum(month_days[:a-1]) + b - 1
    answer = days % 7
    answer = name[str(answer)]
    return answer