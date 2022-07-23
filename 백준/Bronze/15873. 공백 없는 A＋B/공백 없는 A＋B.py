number = input()

if len(number) == 2:
    print(sum(map(int, list(number))))
elif len(number) == 3:
    if number[1] == '0':
        print(10 + int(number[-1]))
    else:
        print(int(number[0]) + 10)
elif len(number) == 4:
    print(20)