from collections import Counter

colors = [] 
nums = []
for _ in range(5):
    c, n = input().split()
    colors.append(c)
    nums.append(int(n))

col_cnt = Counter(colors)
nums_cnt = Counter(nums)

result = 0
if len(col_cnt) == 1 and (max(nums) - min(nums) == 4):
    result = max(nums) + 900
elif 4 in nums_cnt.values():
    for num, cnt in nums_cnt.items():
        if cnt == 4:
            result = num + 800
elif 3 in nums_cnt.values() and 2 in nums_cnt.values():
    for num, cnt in nums_cnt.items():
        if cnt == 3:
            result += num * 10 
        elif cnt == 2:
            result += num
    result += 700
elif 5 in col_cnt.values():
    result += max(nums) + 600
elif max(nums) - min(nums) == 4:
    result = max(nums) + 500
elif 3 in nums_cnt.values():
    for num, cnt in nums_cnt.items():
        if cnt == 3:
            result = num + 400
elif len(nums_cnt) == 3 and 2 in nums_cnt.values():
    temp = []
    for num, cnt in nums_cnt.items():
        if cnt == 2:
            temp.append(num)
    result = max(temp) * 10 + min(temp) + 300
elif 2 in nums_cnt.values():
    for num, cnt in nums_cnt.items():
        if cnt == 2:
            result = num + 200
else:
    result = max(nums) + 100

print(result)