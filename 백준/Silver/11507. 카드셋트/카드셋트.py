def append_card(cards, card_sort):
    kind = {'P': 13, 'K': 13, 'H': 13, 'T': 13}
    for card in cards:
        if card in card_sort[card[0]]:
            return ['GRESKA']
        else:
            card_sort[card[0]].append(card)
    
    result = []
    for k in kind:
        result.append(kind[k] - len(card_sort[k]))
    
    return result

card_sort = {'P': [], 'K': [], 'H': [], 'T': []}
answer = ''

string = input()
cards = [string[i: i+3] for i in range(0, len(string), 3)]
result = append_card(cards, card_sort)
print(*result)