def function(x, c_list):
    result = 0
    for i, c in enumerate(c_list):
        result += c * (x ** i)
        
    return result

def integral(b, a, c_list):
    area = 0
    for i, c in enumerate(c_list):
        i += 1
        area += c * (b ** i - a ** i)/ i

    return area
        
def calculate(a, b, n, e, c_list):
    area = 0
    delta = (b - a) / n
    for i in range(n):
        x = (a + i * delta + e) * delta
        area += function(x, c_list)
    
    return area

k = int(input())
c_list = sorted(list(map(int, input().split())))
a, b, n = map(int, input().split())

s = 0
e = (b - a) / n
area_org = integral(b, a, c_list)
area_new = 10 ** 10
while abs(area_org - area_new) > 10**(-4):
    middle = (s + e) / 2
    area_new = calculate(a, b, n, middle, c_list)
    if area_new > area_org:
        e = middle
    else:
        s = middle
        
print(middle)