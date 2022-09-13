def calc_location(n, idx):
    x = idx // n
    y = idx % n

    return (x, y)

def make_row(n, idx):
    return [idx+1] * idx + list(range(idx+1, n+1))
    
def solution(n, left, right):
    left_loc = calc_location(n, left)
    right_loc = calc_location(n, right)

    if right_loc[0] == left_loc[0]:
        row = make_row(n, right_loc[0])[left_loc[1]: right_loc[1]+1]
    else:
        row = []
        for i in range(left_loc[0], right_loc[0]+1):
            if i == left_loc[0]:
                row.extend(make_row(n, left_loc[0])[left_loc[1]: ])
            elif i == right_loc[0]:
                row.extend(make_row(n, right_loc[0])[:right_loc[1]+1])
            else:
                row.extend(make_row(n, i))
            
    return row