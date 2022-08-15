import sys

n = int(input())
arr = list(float(sys.stdin.readline()) for _ in range(n))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i] * arr[i - 1])
print(f'{max(arr):.3f}')