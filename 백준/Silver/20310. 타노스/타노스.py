from collections import Counter
seq = input()

cnt = dict(Counter(seq))
half_cnt = {k: v//2 for k, v in cnt.items()}

new_seq = []
for s in seq:
    if s == '1':
        if half_cnt[s] > 0:
            half_cnt[s] -= 1
        else:
            new_seq.append(s)
    else:
        if half_cnt[s] > 0:
            new_seq.append(s)
            half_cnt[s] -= 1

print(''.join(new_seq))