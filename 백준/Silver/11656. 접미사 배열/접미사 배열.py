from collections import deque

word = deque(input())
result = set()

while word:
    result.add(''.join(word))
    word.popleft()

result = sorted(result)
print(*result, sep='\n')