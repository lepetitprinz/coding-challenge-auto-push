from math import ceil

def solution(n, words):
    answer = [0, 0]
    
    idx = 0
    hist = [words[0]]
    for word in words[1:]:
        idx += 1
        if (word in hist) or (hist[-1][-1] != word[0]):
            number = (idx + 1) % n
            if number == 0:
                number += n
            rounds = int(ceil((idx + 1) / n))
            answer = [number, rounds]
            break
        
        hist.append(word)
    
    return answer