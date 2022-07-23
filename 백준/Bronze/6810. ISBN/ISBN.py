base = '9780921418'
for _ in range(3):
    base += input()
    
result = 0
for i, num in enumerate(base):
    if i % 2 == 0:
        result += int(num) * 1
    else:
        result += int(num) * 3
print(f'The 1-3-sum is {result}')