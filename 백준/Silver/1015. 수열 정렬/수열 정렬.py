n = int(input())
nums = list(map(int, input().split()))

num_map = {}
for i, num in enumerate(nums):
    if num in num_map:
        num_map[num].append(i)
    else:
        num_map[num] = [i]
num_map = sorted(num_map.items(), key=lambda x: x[0])
        
result = [0] * n
temp = 0
for k, nums in num_map:
    for num in nums:
        result[num] = temp
        temp += 1

print(*result)