import sys
n = int(input())
students = [sys.stdin.readline().rstrip() for _ in range(n)]
length = len(students[0])

for i in range(1, length+1):
    memory = set()
    flag = True
    for student in students:
        sliced = student[-i:]
        if sliced in memory:
            flag = False
            break
        else:
            memory.add(sliced)
    
    if flag:
        break
print(i)