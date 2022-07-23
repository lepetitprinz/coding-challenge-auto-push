def add_adjecent_number(nums):
    result = ''
    for i in range(len(nums) - 1):
        add = str(int(nums[i]) + int(nums[i+1]))
        result += add[-1]
    
    return result

a = input()
b = input()
nums = ''
for i, j in zip(list(a), list(b)):
    nums += i
    nums += j
    
while len(nums) > 2:
    nums = add_adjecent_number(nums)
print(nums)