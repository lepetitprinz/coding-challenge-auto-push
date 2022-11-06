cards = list(map(int, input().split()))
l = len(set(cards))
if l == 1:
    print(cards[0])
else:
    print(max(cards))