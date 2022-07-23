def get_width(i):
    if i ==  0:
        length = 4
    elif i == 1:
        length = 2
    else:
        length = 3
    return length
        
while True:
    number = input()
    if number == '0':
        break
    else:
        serial = list(number)
        serial_width = sum(get_width(int(i)) for i in serial)
        print(serial_width + len(serial) + 1)