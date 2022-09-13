def solution(s):
    answer = True
    
    if (len(s) != 4 and len(s) != 6):
        answer = False
        
    for element in s:
        try: 
            eval(element)
        except:
            answer= False
            break
    
    return answer