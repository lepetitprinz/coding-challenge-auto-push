x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    inclination1 = 'inf'
else:
    inclination1 = (y2 - y1) / (x2 - x1)
if x2 == x3:
    inclination2 = 'inf'
else:
    inclination2 = (y3 - y2) / (x3 - x2)
    
if inclination1 == inclination2:
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')