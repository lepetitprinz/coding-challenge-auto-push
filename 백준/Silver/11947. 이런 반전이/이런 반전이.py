t = int(input())
for _ in range(t):
    n = input()
    start = 10 ** (len(n)-1)
    if int(n) >= 5 * start - 1:
        print(5*start * (5*start - 1))
    else:
        rev = []
        for num in n:
            rev.append(str(9-int(num)))
        rev = int(''.join(rev))
    
        print(int(n) * rev)