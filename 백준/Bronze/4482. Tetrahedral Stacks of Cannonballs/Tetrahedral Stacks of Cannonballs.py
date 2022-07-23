import sys

test = int(input())

for i in range(test):
    n = int(sys.stdin.readline())
    amount = 0
    temp = 0
    for j in range(1, n+1):
        temp += j
        amount += temp
    print(f'{i+1}: {n} {amount}')