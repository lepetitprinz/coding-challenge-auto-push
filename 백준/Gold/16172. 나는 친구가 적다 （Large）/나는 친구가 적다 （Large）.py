import re

a = input()
b = input()
find = re.findall(b, re.sub("[0-9]","",a))

if find:
    print(1)
else:
    print(0)
