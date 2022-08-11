import sys

def action(switch, kind, idx, conv, length):
    if kind == 1:
        for i in range(idx-1, length, idx):
            switch[i] = conv[switch[i]]
    else:
        switch[idx - 1] = conv[switch[idx - 1]]
        for i in range(1, length // 2 + 1):
            if (idx - i - 1) >= 0 and (idx + i - 1) < length:
                if switch[idx - i - 1] == switch[idx + i - 1]:
                    switch[idx - i - 1] = conv[switch[idx - i - 1]]
                    switch[idx + i - 1] = conv[switch[idx + i - 1]]
                else:
                    break
            else:
                break
    return switch

conv = {1: 0, 0: 1}
n = int(input())
switch = list(map(int, input().split()))
length = len(switch)
s = int(input())

for _ in range(s):
    kind, value = map(int, sys.stdin.readline().split())
    switch = action(switch, kind, value, conv, length)

cnt = length // 20 + 1
for i in range(cnt):
    print(*switch[20 * i:20 * (i+1)])
