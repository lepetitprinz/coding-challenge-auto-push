def dp(n):
    d = [[1] * i for i in range(1, n + 1)]
    for i in range(1, n):
        for j in range(1, i):
            d[i][j] = d[i-1][j-1] + d[i-1][j]
    
    return d

def sum_triangle(data, row_start, row_end, start_index):
    total = 0
    end_index = start_index + 1
    for i in range(row_start, row_end):
        for j in range(start_index, end_index):
            total += data[i][j]
        end_index += 1
    
    return total

r, c, w = map(int, input().split())
pascal = dp(r + w - 1)
result = sum_triangle(pascal, r-1, r + w -1, c-1)
print(result)