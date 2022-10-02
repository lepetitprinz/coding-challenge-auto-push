m = int(input())
d = int(input())

result = ''
if m < 2:
    result = 'Before'
elif m > 2:
    result = 'After'
else:
    if d < 18:
        result = 'Before'
    elif d > 18:
        result = 'After'
    else:
        result = 'Special'
        
print(result)