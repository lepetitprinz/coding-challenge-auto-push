n, m = map(int, input().split())
data = sorted([int(input()) for _ in range(m)])

max_price = 0
max_sales = 0
for i, price in enumerate(data):
    sales = price * min(n, m - i)
    if sales > max_sales:
        max_price = price
        max_sales = sales
    
print(max_price, max_sales)