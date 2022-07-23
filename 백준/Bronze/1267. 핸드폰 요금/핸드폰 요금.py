def get_price(number, kind):
    price = 0
    if kind == 'Y':
        price = (number // 30 + 1) * 10
    elif kind == 'M':
        price = (number // 60 + 1) * 15
    
    return price

n = int(input())
calls = list(map(int, input().split()))
y_p = sum([get_price(call, 'Y') for call in calls])
m_p = sum([get_price(call, 'M') for call in calls])

if y_p < m_p:
    print(f'Y {y_p}')
elif y_p > m_p:
    print(f'M {m_p}')
else:
    print(f'Y M {y_p}')