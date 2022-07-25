n = int(input())
data = list(map(int, input().split()))
if n == 1:
    print(1)
else:
    asc_list = []
    des_list = []
    ascend = 1
    descend = 1
    prev = data[0]
    for num in data[1:]:
        if num >= prev:
            ascend += 1 
        else:
            asc_list.append(ascend)
            ascend = 1
        if num <= prev:
            descend += 1
        else:
            des_list.append(descend)
            descend = 1
        prev = num
    asc_list.append(ascend)
    des_list.append(descend)

    print(max(asc_list + des_list))