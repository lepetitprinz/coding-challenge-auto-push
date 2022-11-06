s, k, h = map(int, input().split())
if s+k+h >= 100:
    print('OK')
else:
    min_val = min(s, k, h)
    if s == min_val:
        print('Soongsil')
    elif k == min_val:
        print('Korea')
    else:
        print('Hanyang')