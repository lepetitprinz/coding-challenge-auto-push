def calc_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    return width * height
    
def compare_location(a1, a2, a3, a4):
    length = 0
    if a2 > a4:
        if a1 > a3:
            length = a4 - a1
        else:
            length = a4 - a3
    else:
        if a1 > a3:
            length = a2 - a1
        else:
            length = a2 - a3
    
    return length
    
t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    area1 = calc_area(p1=(x1, y1), p2=(x2, y2))
    
    if x3 >= x2 or y3 >= y2 or x1 > x4 or y1 > y4:
        result = area1
    else:
        width = compare_location(x1, x2, x3, x4)
        height = compare_location(y1, y2, y3, y4)
        area2 = width * height
        result = area1 - area2
    
    print(result)