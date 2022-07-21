w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

t_w = (p + t) % w
t_h = (q + t) % h

w_div = (p + t) // w
h_div = (q + t) // h

if w_div % 2 == 0:
    x = t_w
else:
    x = w - t_w
    
if h_div % 2 == 0:
    y = t_h
else:
    y = h - t_h

print(f'{x} {y}')