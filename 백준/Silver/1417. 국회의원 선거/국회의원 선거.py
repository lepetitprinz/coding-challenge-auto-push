n = int(input())
person = int(input())
other = [int(input()) for _ in range(n-1)]

cnt = 0
while n > 1:
    if person > max(other):
        break
    else:
        other[other.index(max(other))] -= 1
        person += 1
        cnt += 1
        
print(cnt)