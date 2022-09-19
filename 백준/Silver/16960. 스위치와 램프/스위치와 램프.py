import sys

def check(switches, switche_cnt):
    result = 0
    for switch in switches:
        flag = True
        for val in switch:
            if switche_cnt.get(val, 0) == 1:
                flag = False
                break
        if flag:
            result = 1
            break

    return result

n, m = map(int, input().split())

switch_cnt = {}
switches = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    if data[0] != 0:
        vals = data[1:]
        switches.append(vals)
        for val in vals:
            if val in switch_cnt:
                switch_cnt[val] += 1
            else:
                switch_cnt[val] = 1
    else:
        switches.append([0])

result = check(switches, switch_cnt)
print(result)