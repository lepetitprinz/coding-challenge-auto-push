a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
diff = sorted(list(set_a - set_b))
if len(diff) == 0:
    print(0)
else:
    print(len(diff))
    print(*diff)