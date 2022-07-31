import sys

def car_mapping(car_map, region):
    for r, nums in car_map.items():
        nums = sorted(nums, reverse=True)
        people = region.get(r, [])
        for num in nums:
            if 'S' in people:
                people.remove('S')
                num -= 1
                for _ in range(num):
                    if 'I' in people:
                        people.remove('I')
                    elif 'S' in people:
                        people.remove('S')
    
    remain = 0
    for r, p in region.items():
        remain += len(p)
    
    return remain

test = int(input())
for i in range(1, test + 1):
    n, c, l = map(int, sys.stdin.readline().split())
    region = {}
    car_map = {}
    for _ in range(n):
        r, s = sys.stdin.readline().split()
        if int(r) in region:
            region[int(r)].append(s)
        else:
            region[int(r)] = [s] 
            
    for _ in range(c):
        car, number = map(int, sys.stdin.readline().split())
        if car in car_map:
            car_map[car].append(number)
        else:
            car_map[car] = [number]
            
    result = car_mapping(car_map, region)
    print(f'Data Set {i}:')
    print(result)