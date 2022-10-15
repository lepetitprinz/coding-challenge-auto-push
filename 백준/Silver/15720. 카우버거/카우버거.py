b, c, d = map(int, input().split())

b_list = sorted(list(map(int, input().split())), reverse=True)
c_list = sorted(list(map(int, input().split())), reverse=True)
d_list = sorted(list(map(int, input().split())), reverse=True)

org_price = sum(b_list) + sum(c_list) + sum(d_list)

discount_cnt = min(b, c, d)
discount_price = 0
for i in range(discount_cnt):
    discount_price += b_list[i] * 0.9
    discount_price += c_list[i] * 0.9
    discount_price += d_list[i] * 0.9

for kind in [b_list, c_list, d_list]:
    if len(kind) > discount_cnt:
        discount_price += sum(kind[discount_cnt:])

print(org_price)
print(int(discount_price))