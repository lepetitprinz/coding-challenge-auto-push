import sys
from collections import Counter

i = 0
sentence = ''
while i < 50:
    try:
        sentence += sys.stdin.readline().rstrip().replace(' ','')
        i += 1
    except:
        break
        
alpha_cnt = Counter(sentence)
max_cnt_alphabet = sorted(alpha_cnt.items(), key=lambda x: (-x[1], x[0]))
max_cnt = max_cnt_alphabet[0][1]
result = ''
for k, v in max_cnt_alphabet:
    if max_cnt == v:
        result += k
print(result)