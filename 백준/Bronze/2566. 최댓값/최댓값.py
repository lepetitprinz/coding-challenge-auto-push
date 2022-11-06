max_num = 0
loc = [0,0]
for i in range(9):
    nums = list(map(int, input().split()))
    for j, num in enumerate(nums):
        if max_num <= num:
            max_num = num
            loc = [i+1, j+1]
print(max_num)
print(*loc)