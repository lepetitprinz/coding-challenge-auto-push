from math import ceil

n, a, b = map(int, input().split())
semesters = [map(int, input().split()) for _ in range(10)]

s = 8 - n
major = 66 - a
remain = 130 - b

flag = False
for m, r in semesters[:s]:
    s_tot = 6
    if major > 0:
        m_need = ceil(major / 3)
        m_use = min(m, m_need)
        s_tot -= m_use
        major -= m_use * 3
        remain -= m_use * 3
        
    remain -= min(s_tot, r) * 3
        
if major > 0 or remain > 0:
    print('Nae ga wae')
else:
    print('Nice')