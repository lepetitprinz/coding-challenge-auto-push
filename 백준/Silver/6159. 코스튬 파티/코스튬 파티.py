import sys

n, s = map(int, input().split())
data = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse=True)

count = 0
for i, cow1 in enumerate(data):
    for j, cow2 in enumerate(data[i+1:]):
        gap = s - cow1
        if gap > 0:
            if cow2 <= gap:
                count += n - j -i - 1
                break

print(count)