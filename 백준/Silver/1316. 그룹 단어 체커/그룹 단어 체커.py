import sys

def check(string):
    memory = []
    for i in range(len(string)-1):
        if string[i+1] in memory:
            return False
        if string[i+1] == string[i]:
            continue
        else:
            memory.append(string[i])
    
    return True

n = int(input())
cnt = 0
for _ in range(n):
    cnt += check(sys.stdin.readline())
print(cnt)