n = int(input())
if n == 0:
    print(1)
elif n == 1:
    print(0)
else:
    div = n // 2
    mod = n % 2
    if mod == 0:
        print('8' * div)
    else:
        print('4' + '8' * div)