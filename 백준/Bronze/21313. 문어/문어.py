n = int(input())
result = ''
if n % 2 == 0:
    result += '12' * (n//2)
else:
    result += '12' * (n//2) + '3'

print(' '.join(result))