def calc_budget(start, end, res, overs, best):
    if start > end:
        return best
    mid = (start+end)//2
    over = []
    under = 0
    total = 0
    for budget in overs:
        if budget <= mid:
            under += budget
            total += budget
        else:
            over.append(budget)
            total += mid
    if total <= res:
        if best <= mid:
            best = calc_budget(mid+1, end, res-under, over, mid)
    else:
        best = calc_budget(start, mid-1, res, overs, best)
    return best

n = int(input())
budgets = list(map(int, input().split()))
total = int(input())
avg = total // n
max_budget = avg
under = 0
over = []
for budget in budgets:
    if budget <= avg:
        under += budget
    else:
        over.append(budget)
        
res = total - under
best = calc_budget(avg, max(budgets), res, over, avg)
print(best)