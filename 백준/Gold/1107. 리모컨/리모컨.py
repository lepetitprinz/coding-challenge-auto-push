from itertools import product

n = int(input())
m = int(input())
max_move = abs(n - 100)

button = set(map(str, range(0, 10)))
if m != 0:
    button = button - set(list(input().split()))

length = len(str(n))
moves = []
for i in range(1, length + 2):
    for move in product(button, repeat=i):
        m = abs(int(''.join(move)) - n)
        moves.append(m + i)
if len(moves) > 0:
    print(min(max_move, min(moves)))
else:
    print(max_move)