while True:
    try:
        a, b = map(int, input().split())
        cnt = 0
        for i in range(a, b+1):
            if len(str(i)) == len(set(str(i))):
                cnt += 1
        print(cnt)
    except:
        break