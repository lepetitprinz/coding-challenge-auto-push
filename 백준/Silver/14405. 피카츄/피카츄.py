word = input()
word = word.replace('pi', ' ')
word = word.replace('ka', ' ')
word = word.replace('chu', ' ')
word = word.replace(' ', '')

if len(word) == 0:
    print('YES')
else:
    print('NO')