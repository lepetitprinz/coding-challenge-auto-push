word = input()
s_word = input()
s_len = len(s_word)

idx = 0
cnt = 0
while idx < len(word):
    if word[idx: idx + s_len] == s_word:
        cnt += 1
        idx += s_len
    else:
        idx += 1
        
print(cnt)