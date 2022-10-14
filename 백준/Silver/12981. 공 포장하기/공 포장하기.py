def solution(data):
    cnt = 0

    # Step 1
    min_cnt = min(data)
    step1 = []
    for v in data:
        step1.append(v - min_cnt)
    cnt += min_cnt

    # Step 2
    step2 = []
    for v in step1:
        c = v // 3
        step2.append(v - c * 3)
        cnt += c

    # Step 3
    if sum(step2) != 0:
        if sum(step2) in [3, 4]:
            cnt += 2
        else:
            cnt += 1

    return cnt

data = list(map(int, input().split()))
result = solution(data)
print(result)