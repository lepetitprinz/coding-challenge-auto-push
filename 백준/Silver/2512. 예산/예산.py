def binary_search(start, end, target):
    if start > end:
        return start - 1
    
    mid = (start + end) // 2
    money = calc_budget(mid)
    if money > target:
        return binary_search(start, mid - 1, target)
    elif money == target:
        return mid
    else:
        return binary_search(mid + 1, end, target)
    
def calc_budget(line):
    money = 0
    for i, budget in enumerate(budgets):
        if budget <= line:
            money += budget
        else:
            money += line * (n - i)
            break
    
    return money
    
    
n = int(input())
budgets = sorted(list(map(int, input().split())))
threshold = int(input())

result = 0
if sum(budgets) <= threshold:
    result = budgets[-1]
else:
    result = binary_search(0, budgets[-1], threshold)

print(result)