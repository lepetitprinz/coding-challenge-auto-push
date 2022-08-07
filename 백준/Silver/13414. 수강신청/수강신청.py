import sys

k, l = map(int, input().split())
memory = {}
for i in range(l):
    person = sys.stdin.readline().rstrip()
    memory[person] = i

result = sorted(memory.items(), key= lambda x:x[1])
 
cnt = 0
for p, order in result:
    if cnt  <  k:
        print(p)
        cnt += 1
    else:
        break