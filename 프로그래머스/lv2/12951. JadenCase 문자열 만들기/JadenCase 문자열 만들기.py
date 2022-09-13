def solution(s):
    s = s.lower()
    words = s.split(" ")
    
    result = []
    for word in words:
        temp = word.capitalize()
        result.append(temp)
    
    return ' '.join(result)