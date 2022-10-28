n1, n2 = map(int, input().split())
a1 = list(input())
a2 = list(input())
t = int(input())

a1.reverse()
a = a1 + a2
for _ in range(t):
    for i in range(len(a) - 1):
        if a[i] in a1 and a[i + 1] in a2:
            a[i], a[i + 1] = a[i + 1], a[i]
        
            if a[i + 1] == a1[-1]:
                break

print(''.join(a))