def calculate(x, y, w):
    h1 = (x**2 - w**2) ** 0.5
    h2 = (y**2 - w**2) ** 0.5
    
    return h1 * h2 / (h1 + h2)

x, y, c = map(float, input().split())
start = 0
end = min(x, y)
width = 0
while end - start > 0.000001:
    middle = (start + end) / 2
    if calculate(x, y, middle) >= c:
        start = middle
        width = middle
    else:
        end = middle
        
print(width)    