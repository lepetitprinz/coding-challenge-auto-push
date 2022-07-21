from string import ascii_lowercase

vowel =  ['a', 'e', 'i', 'o', 'u']
consonant = set([w for w in ascii_lowercase if w not in vowel])
vowel = set(vowel)

def check(word):
    flag = False
    if len(set(word).intersection(vowel)) > 0:
        if check_seq(word):
            if check_seq_2(word):
                flag = True
    
    return flag

def check_seq(word):
    flag = True
    for i in range(len(word)-2):
        temp = word[i: i+3]
        if set(temp).issubset(vowel) or set(temp).issubset(consonant):
            flag = False
            break
    
    return flag

def check_seq_2(word):
    flag = True
    temp = word[0]
    for w in word[1:]:
        if w == temp[-1]:
            if w == 'e' or w == 'o':
                continue
            else:
                flag = False
                break
        else:
            temp = w
    
    return flag

while True:
    word = input()
    if word == 'end':
        break
    else:
        if check(word):
            print(f'<{word}> is acceptable.')
        else:
            print(f'<{word}> is not acceptable.')