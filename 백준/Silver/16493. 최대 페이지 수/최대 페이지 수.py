import sys

input = lambda: sys.stdin.readline().rstrip()

def dp(due, chapters, days, pages):
    d = [[0] * (due + 1) for _ in range(chapters + 1)]
    for i in range(1, chapters + 1):
        for j in range(1, due + 1):
            prev = d[i - 1][j]
            if j >= days[i - 1]:
                d[i][j] = max(prev, d[i - 1][j - days[i - 1]] + pages[i - 1])
            else:
                d[i][j] = prev
    
    return d[chapters][due]

due, chapters = map(int, input().split())
days = []
pages = []
for _ in range(chapters):
    d, p = map(int, input().split())
    days.append(d)
    pages.append(p)
    
result = dp(due, chapters, days, pages)
print(result)