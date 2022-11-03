import sys

input = lambda: sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
n = int(input())
checks = [list(map(int, input().split())) for _ in range(n)]

success = set([])
for check in checks:
    if check[3] == 1:
        success.update(check[:3])
        
fail = set([])
for check in checks:
    temp = set(check[:3]) - success
    if len(temp) == 1:
        fail.update(temp)

for i in range(1, a + b + c + 1):
    if i in success:
        print(1)
    elif i in fail:
        print(0)
    else:
        print(2)