string = input()
compare = input()
string = ''.join(s for s in string if s.isalpha())

if compare in string:
    print(1)
else:
    print(0)