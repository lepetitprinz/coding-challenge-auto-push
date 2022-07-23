flag = True
angles = []
for _ in range(3):
    angle = int(input())
    angles.append(angle)
    if angle != 60:
        flag = False

if flag:
    print('Equilateral')
else:
    if sum(angles) == 180:
        if len(set(angles)) == 2:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print("Error")