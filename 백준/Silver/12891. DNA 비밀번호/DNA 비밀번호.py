from collections import deque
from collections import Counter

def compare(cnt, sub_seq_cnt):
    flag = 1
    for k, v in cnt.items():
        if sub_seq_cnt.get(k, 0) < v:
            flag = 0
            break

    return flag

def update_sub_seq_cnt(sub_seq_cnt, rm, add):
    sub_seq_cnt[rm] -= 1
    if add not in sub_seq_cnt:
        sub_seq_cnt[add] = 1
    else:
        sub_seq_cnt[add] += 1
    
    return sub_seq_cnt

s, p = map(int, input().split())
seq = input()
cnt = list(map(int, input().split()))
cnt = {dna: val for dna, val in zip(['A', 'C', 'G', 'T'], cnt)}

sub_seq = seq[:p]
sub_seq_cnt = dict(Counter(sub_seq))
queue = deque(sub_seq)

result = compare(cnt, sub_seq_cnt)
for s in seq[p:]:
    remove_dna = queue.popleft()
    sub_seq_cnt = update_sub_seq_cnt(sub_seq_cnt, remove_dna, s)
    result += compare(cnt, sub_seq_cnt)
    queue.append(s)

print(result) 