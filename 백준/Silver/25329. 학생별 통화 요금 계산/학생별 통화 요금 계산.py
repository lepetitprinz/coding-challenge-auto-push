import sys
from math import ceil

input = lambda: sys.stdin.readline().rstrip()

def calc_fee(time):
    fee = 10
    time = max(0, time - 100)
    fee += ceil(time / 50) * 3

    return int(fee)

n = int(input())
fee = {}
for _ in range(n):
    time, name = input().split()
    h, m = map(int, time.split(':'))
    tot_time = h * 60 + m
    if name in fee:
        fee[name] += tot_time
    else:
        fee[name] = tot_time

result = [[name, calc_fee(time)] for name, time in fee.items()]
result = sorted(result, key=lambda x: (-x[1], x[0]))
for name, time in result:
    print(name, time)