def binary_search(start, end, target):
    if start > end:
        return start
    
    mid = (start + end) // 2
    
    mid_val = result[mid]
    if mid_val > target:
        return binary_search(start, mid - 1, target)

    elif mid_val == target:
        return mid
    else:
        return binary_search(mid + 1, end, target)
    
n = int(input())
data = list(map(int, input().split(" ")))


result = [data[0]]
for i in range(1, n):
    value = data[i]
    if result[-1] < value:
        result.append(value)
    else:
        idx = binary_search(0, len(result) - 1, value)
        result[idx] = value
        
print(len(result))