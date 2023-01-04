import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

grade = 0
stack = []

for _ in range(n):
    assignment = list(map(int, input().split()))
    if len(assignment) == 1:
        if len(stack) > 0:
            a, t = stack.pop()
            t -= 1
            if t == 0:
                grade += a
            else:
                stack.append([a, t])
    else:
        a = assignment[1]
        t = assignment[2]
        t -= 1
        if t == 0:
            grade += a
        else:
            stack.append([a, t])
    
print(grade)