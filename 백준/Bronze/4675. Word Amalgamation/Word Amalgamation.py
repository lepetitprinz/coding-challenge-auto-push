from itertools import permutations


def search_unscramble_word(word, dictionary):
    unscramble_word = []
    for w in permutations(word, len(word)):
        w = ''.join(w)
        if w in dictionary:
            if w not in unscramble_word:
                unscramble_word.append(w)

    return sorted(unscramble_word)


dictionary = set()
while True:
    word = input().rstrip()
    if word == 'XXXXXX':
        break
    else:
        dictionary.add(word)
while True:
    word = input().rstrip()
    if word == 'XXXXXX':
        break
    else:
        result = search_unscramble_word(word, dictionary)
        if len(result) == 0:
            print("NOT A VALID WORD")
        else:
            for r in result:
                print(r)
        print("******")