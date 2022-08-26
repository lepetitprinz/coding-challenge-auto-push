word = input()
cnt = 0
while len(word) > 1:
    word = sum(map(int, list(word)))
    word = str(word)
    cnt += 1

number = int(word)
if number % 3 == 0:
    result = 'YES'
else:
    result = 'NO'
    
print(cnt)
print(result)