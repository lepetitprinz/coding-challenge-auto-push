import sys
input = lambda: sys.stdin.readline().rstrip()

def sliding_window(arr, i, j, w):
    window = []
    for r in range(i, i + w):
        for c in range(j, j + w):
            window.append(arr[r][c])
    return window


def get_median(window, w):
    window = sorted(window)
    median = window[w**2 // 2]

    return median


m, n, k, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

for i in range(m - w + 1):
    row = []
    for j in range(n - w + 1):
        window = sliding_window(arr, i, j, w)
        median = get_median(window, w)
        row.append(median)
    print(*row)