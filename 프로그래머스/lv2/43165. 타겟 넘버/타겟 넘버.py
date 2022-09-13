from collections import deque

def solution(numbers, target):
    answer = 0
    length = len(numbers)
    
    queue = deque([(0, 0)])
    while queue:
        total, level = queue.popleft()
        if level > length:
            break
        if level == length and total == target:
            answer += 1
        queue.append((total + numbers[level-1], level+1))
        queue.append((total - numbers[level-1], level+1))
        
    return answer