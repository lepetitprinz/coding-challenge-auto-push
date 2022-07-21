n = int(input())
seq = list(map(int, input().split()))

line = list(range(1, n+1))
for i, s in enumerate(seq):
    move_index = i - s
    move_val = line.pop(i)
    line = line[:move_index] + [move_val] + line[move_index:]
            
line = [str(l) for l in line]
print(' '.join(line))