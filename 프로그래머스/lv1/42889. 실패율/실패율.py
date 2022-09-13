from collections import Counter

def solution(N, stages):
    count, cum_cnt = set_count_and_cum_count(n=N, stages=stages)
    fail_rate = calc_fail_rate(n=N, count=count, cum_cnt=cum_cnt)
    result = get_order(fail_rate=fail_rate)
    
    return result

def set_count_and_cum_count(n, stages):
    count_map = dict(Counter(stages))
    cum_count_map = {}
    for i in range(n+1, 0, -1):
        cnt = count_map.get(i, 0)
        if i == n+1:
            cum_cnt = cnt
        else:
            cum_cnt = cum_count_map[i+1] + cnt
        cum_count_map[i] = cum_cnt

    return count_map, cum_count_map

def calc_fail_rate(n, count, cum_cnt):
    fail_rate = []
    for i in range(1, n+1):
        if cum_cnt[i] == 0:
            rate = 0
        else:
            rate = count.get(i,0) / cum_cnt[i]
        fail_rate.append((i, rate))
    
    return fail_rate

def get_order(fail_rate):
    fail_rate = sorted(fail_rate, key=lambda x: (-x[1], x[0]))
    order = [num for num, rate in fail_rate]
    
    return order