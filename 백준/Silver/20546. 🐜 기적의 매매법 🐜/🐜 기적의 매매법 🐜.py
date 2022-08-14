def stock(money, price, method):
    history = []
    if method == 'bnp':
        for p in price:
            if money >= p:
                number = money // p
                history.append([p, number])
                money -= p * number

        result = [[p, number] for h, number in history]

    else:
        inc = 1
        dec = 1
        prev = price[0]
        for p in price[1:]:
            if inc == 3:
                if len(history) > 0:
                    money += sum(p * n for h, n in history)
                    history = []
            elif dec == 3:
                if money >= p:
                    number = money // p
                    history.append([p, number])
                    money -= p * number
                    
            dec, inc = update_seq(p, prev, dec, inc)
            prev = p

        result = [[p, number] for h, number in history]

    return result, money


def update_seq(p, prev, dec, inc):
    if p > prev:
        inc += 1
        dec = 1
    elif p < prev:
        dec += 1
        inc = 1
    else:
        inc = 1
        dec = 1

    return min(dec, 3), min(inc, 3)


money = int(input())
price = list(map(int, input().split()))

h1, m1 = stock(money, price, 'bnp')
h2, m2 = stock(money, price, 'timing')

bnp = sum(p1 * n1 for p1, n1 in h1) + m1
timing = sum(p2 * n2 for p2, n2 in h2) + m2

if bnp > timing:
    print('BNP')
elif bnp < timing:
    print('TIMING')
else:
    print('SAMESAME')