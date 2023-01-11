a, b, n = map(int, input().split())
s = []
pack = {'B':a, 'R':b}
time = {'B':0, 'R':0}
count = {'B':0, 'R':0}
for _ in range(n):
    t, color, cnt = input().split()
    t = int(t)
    cnt = int(cnt)
    count[color] += cnt
    for i in range(cnt):
        if t < time[color]:
            t = time[color]
        s.append((t, color))
        t += pack[color]
    time[color] = t
    
s = sorted(s)
nums = {'B':[], 'R':[]}
for i in range(len(s)):
    nums[s[i][1]].append(i+1)
    
print(count['B'])
print(*nums['B'])
print(count['R'])
print(*nums['R'])