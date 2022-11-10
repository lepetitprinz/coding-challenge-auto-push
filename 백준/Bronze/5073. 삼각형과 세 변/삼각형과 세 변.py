while True:
    length = sorted(list(map(int, input().split())))
    if length == [0,0,0]:
        break
    s = set(length)
    l = len(s)
    if length[2] >= length[0] + length[1]:
        print('Invalid')
    elif l == 1:
        print('Equilateral')
    elif l == 2:
        print('Isosceles')
    else:
        print('Scalene')