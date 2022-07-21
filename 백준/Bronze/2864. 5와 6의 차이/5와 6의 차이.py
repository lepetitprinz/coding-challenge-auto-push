a, b = input().split()
a_min, b_min = a.replace('6', '5'), b.replace('6', '5')
a_max, b_max = a.replace('5', '6'), b.replace('5', '6')
print(f'{int(a_min) + int(b_min)} {int(a_max) + int(b_max)}')