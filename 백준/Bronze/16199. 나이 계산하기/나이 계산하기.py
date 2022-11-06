y, m, d = map(int, input().split())
by, bm, bd = map(int, input().split())
if bm > m or (bm == m and bd >= d):
    print(by-y)
else:
    print(by-y-1)
print(by-y+1)
print(by-y)