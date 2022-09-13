def solution(n):
    chg_map = {'0':'1', '1': '2', '2': '4'}
    converted = convert(n, 3)
    result = [chg_map[string] for string in converted]
    
    return ''.join(result)
    
def convert(n, d):
    result = ''
    while n:
        num = n - 1
        result = str(num % d) + result
        n = num // d
        
    return result