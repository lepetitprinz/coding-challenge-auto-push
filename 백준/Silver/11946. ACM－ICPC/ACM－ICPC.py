import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())
times = {}
ac_nums = {}
failed = {}
for i in range(n):
    times[i+1] = 0
    ac_nums[i+1] = set()
    failed[i+1] = dict()
    
for _ in range(q):
    ls = input().split()
    time, team, question = map(int, ls[:3])
    rst = ls[3]
    
    if rst == 'AC':
        if question not in ac_nums[team]:
            times[team] += failed[team].get(question, 0) * 20 + time
            ac_nums[team].add(question)
    else:
        fail = failed[team].get(question, 0)
        failed[team][question] = fail + 1
    
rank = sorted(list(range(1, n+1)), key=lambda x: [-len(ac_nums[x]), times[x]])

for rnk in rank:
    print(rnk, len(ac_nums[rnk]), times[rnk])