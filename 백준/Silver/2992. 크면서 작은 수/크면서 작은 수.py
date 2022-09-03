from itertools import permutations

n = input()
value = int(n)
nums = set(permutations(list(n), len(n)))
nums = sorted(list(nums))
temp = 0
for num in nums:
    if int(''.join(num))  > value:
        temp = int(''.join(num))
        break
print(temp)