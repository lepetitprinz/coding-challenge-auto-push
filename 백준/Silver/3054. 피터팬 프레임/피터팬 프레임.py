word = input()
length = len(word)
frame_length = 5 + (length - 1) * 4

frame = [['.'] * frame_length for _ in range(5)]
start_index = [2, 1, 0, 1, 2]
add_index = [4, 2, 2, 2, 4]


# add simbol on frame
for i, line in enumerate(frame):
    idx = start_index[i]
    add_idx = add_index[i]
    
    while idx < frame_length:
        simbol = '#'
        if i in [0, 1, 3, 4]:
            if (idx // 4 + 1) % 3 == 0:
                simbol = '*'
        if i == 2 and idx != 0:
            if (idx // 4 + 1) % 3 == 0 or (idx % 4 == 0 and (idx // 4) % 3 == 0):
                simbol = '*'
        
            if length % 3 != 0 and idx == frame_length - 1:
                simbol = '#'
        
        line[idx] = simbol
        idx += add_idx

for i, char in enumerate(word):
    loc = i * 4 + 2
    frame[2][loc] = char
        
for line in frame:
    print(''.join(line))