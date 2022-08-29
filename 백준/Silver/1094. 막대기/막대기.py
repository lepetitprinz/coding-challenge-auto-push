n = int(input())
curr = [64]
while True:
    if sum(curr) == n:
        break
    else:
        min_val = min(curr)
        min_half_val = min_val // 2
        if sum(curr) - min_half_val >= n:
            curr.remove(min_val)
            curr.append(min_half_val)
        else:
            curr.remove(min_val)
            curr.extend([min_half_val, min_half_val])

print(len(curr))