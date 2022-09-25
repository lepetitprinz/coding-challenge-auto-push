x, y = map(int, input().split())
half_size = 125 ** 2

result = []
if x == 0:
    if y >= 125:
        answer = round(half_size * 2 / y, 2)
        result = [answer, 0]
    else:
        answer_x = round(half_size * 2 / (250 - y), 2)
        answer_y = 250 - answer_x
        result = [answer_x, answer_y]
elif y == 0:
    if x >= 125:
        answer = round(half_size * 2 / x, 2)
        result = [0, answer]
    else:
        answer_y = round(half_size * 2 / (250 - x), 2)
        answer_x = 250 - answer_y
        result = [answer_x, answer_y]
else:
    if x >= 125:
        answer = 250 - round(half_size * 2 / x, 2)
        result = [0, answer]
    else:
        answer = 250 - round(half_size * 2 / y, 2)
        result = [answer, 0]
        
print(f'{result[0]:.2f} {result[1]:.2f}')