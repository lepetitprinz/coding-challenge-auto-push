start = list(input())
target = list(input())

while len(start) != len(target):
    if target[-1] == 'A':
        target.pop()
    else:
        target.pop()
        target.reverse()

if start == target:
    print(1)
else:
    print(0)