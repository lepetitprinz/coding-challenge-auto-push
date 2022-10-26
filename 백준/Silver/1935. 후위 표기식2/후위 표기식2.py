import sys
from string import ascii_uppercase

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
equation = input()
alphabet = ascii_uppercase
values = {alphabet[i]: input() for i in range(n)}

arithmetic = ['+', '-', '*', '/']
stack = []
for e in equation:
    if e in arithmetic:
        back = stack.pop()
        front = stack.pop()
        value = eval(front + e + back)
        stack.append(str(value))
    else:
        stack.append(values[e])

result = float(stack.pop())
print(f"{result:.2f}")