import re

n = int(input())
num = re.compile(r'\d+')
numbers = []
for _ in range(n):
    numbers.extend(list(map(int, num.findall(input()))))
    
numbers = sorted(numbers)
print(*numbers, sep='\n')