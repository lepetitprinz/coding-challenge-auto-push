n = int(input())
string = input()
print(f'#define quadtree_width {n}')
print(f'#define quadtree_height {n}')
fixels = [['']*n for _ in range(n)]

def daq(start_r, start_c, length, string, end):
    if string[end] == 'Q':
        l = length // 2
        for i in range(2):
            for j in range(2):
                end = daq(start_r+(l*i), start_c+(l*j), l, string, end+1)
    else:
        if string[end] == 'W':
            s = '0'
        else:
            s = '1'
        for i in range(length):
            fixels[start_r+i][start_c:start_c+length] = [s] * length
    return end


end = daq(0, 0, n, string, 0)
print('static char quadtree_bits[] = {')
for i in range(n):
    for j in range(0,n,8):
        conv = hex(int('0b'+''.join(fixels[i][j:j+8][::-1]), 2))
        conv = conv[:2] + conv[2:].zfill(2)
        print(conv, end=',')
    print()
print('};')