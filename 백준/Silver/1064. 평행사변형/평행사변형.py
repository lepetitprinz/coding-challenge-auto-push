from math import sqrt

def calc_length(p1, p2):
    return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compare(x1, y1, x2, y2, x3, y3):
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    l1 = calc_length(p1, p2)
    l2 = calc_length(p2 ,p3)
    l3 = calc_length(p1, p3)
    result = (max(l1, l2, l3) - min(l1, l2, l3)) * 2
    
    return result

x1, y1, x2, y2, x3, y3 = map(int, input().split())
if (x1 == x2 == x3) or (y1 == y2 == y3):
    result = -1
elif (x1 != x2) & (x2 != x3):
    if (y3-y2) / (x3-x2) == (y2-y1) / (x2-x1):
        result = -1
    else:
        result = compare(x1, y1, x2, y2, x3, y3)
else:
    result = compare(x1, y1, x2, y2, x3, y3)
    
print(result)