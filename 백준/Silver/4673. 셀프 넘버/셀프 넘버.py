nums = []
for i in range(1, 10):
    nums.append(2 * i)
    for j in range(0, 10):
        nums.append(11*i + 2*j)
        for k in range(0, 10):
            nums.append(101*i + 11*j + 2*k)
            for l in range(0, 10):
                nums.append(1001*i + 101*j + 11*k + 2*l)

result = sorted(list(set(range(1, 10001)) - set(nums)))

for r in result:
    print(r)