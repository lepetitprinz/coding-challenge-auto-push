from math import floor

def solution(x, y, v_list):
    time = [x / v for v in v_list]
    min_time = min(time[:-1])
    z = v_list[-1]

    result = 0
    if min_time <= time[-1]:
        if 1 + (x-y) / z >= min_time:
            result = -1
        else:
            result = x - z * (min_time - 1)
            result = floor(result + 1)

    return result


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    v_list = list(map(int, input().split()))
    answer = solution(x, y, v_list)
    print(answer)