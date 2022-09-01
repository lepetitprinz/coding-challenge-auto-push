n = int(input())
stairs = list(map(int, input().split()))

max_stair = 0
curr_stair = 0
for stair in stairs:
    if stair > curr_stair:
        curr_stair += 1
        max_stair = max(max_stair, curr_stair)
    else:
        curr_stair = stair

print(max_stair)