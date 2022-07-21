options = [500, 100, 50, 10, 5, 1]
change = 1000 - int(input())

result = 0
for option in options:
    if change == 0:
        break
        
    if option <= change:
        cnt = change // option
        change -= option * cnt
        result += cnt

print(result)