channel = int(input())
n = int(input())
button = set(map(str, range(10)))

if n:
    button -= set(input().split())
press = abs(channel-100)

for i in range(press):
    down = set(str(channel - i))
    if button.intersection(down) == down:
        press = min(press,i + len(str(channel-i)))
        break
    up = set(str(channel + i))
    if button.intersection(up) == up:
        press = min(press, i + len(str(channel+i)))
        break
        
print(press)