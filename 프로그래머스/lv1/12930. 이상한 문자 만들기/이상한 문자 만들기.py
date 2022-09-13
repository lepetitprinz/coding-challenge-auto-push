def solution(s):
    words = s.split(' ')
    words_new = []
    for word in words:
        temp = ''
        for i, s in enumerate(word):
            if i % 2 == 0:
                temp += s.upper()
            else:
                temp += s.lower()
        words_new.append(temp)
        
    return ' '.join(words_new)