test = int(input())
for _ in range(test):
    w, k = map(int, input().split())
    print(w * k // 2)