def solve(n):
    arr = [[1] * 10]
    
    for step in range(1, n):
        prev_row = arr[step - 1]
        temp = []
        for i in range(0 , 10):
            val = sum(prev_row[i:]) % 10007
            temp.append(val)
        arr.append(temp)

    return sum(arr[-1]) % 10007

n = int(input())
result = solve(n)
print(result)