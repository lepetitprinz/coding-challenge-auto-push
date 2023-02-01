n, w, h, l = map(int, input().split())
w_cnt = w // l
h_cnt = h // l
ans = min(n, w_cnt * h_cnt)
print(ans)