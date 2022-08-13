word = input()
search = ['U', 'C', 'P', 'C']
for w in word:
    if len(search) == 0:
        break
    else:
        if w == search[0]:
            search.pop(0)

if len(search) == 0:
    print('I love UCPC')
else:
    print('I hate UCPC')