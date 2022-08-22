import sys

n = int(input())
for i in range(n):
    data = list(sys.stdin.readline().split())
    data = data[::-1]
    print(f"Case #{i+1}: {' '.join(data)}")