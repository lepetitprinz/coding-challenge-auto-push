import sys
from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    min_heap = []
    max_heap = []
    memory = {}
    for _ in range(int(sys.stdin.readline().rstrip())):
        action, number = sys.stdin.readline().rstrip().split()
        number = int(number)
        if action == 'I':
            heappush(min_heap, number)
            heappush(max_heap, -number)
            if number in memory:
                memory[number] += 1
            else:
                memory[number] = 1
        else:
            if len(memory) == 0:
                continue
            else:
                while True:
                    if number == 1:
                        value = -heappop(max_heap)
                    else:
                        value = heappop(min_heap)

                    if value in memory:
                        if memory[value] == 1:
                            memory.pop(value)
                        else:
                            memory[value] -= 1
                        break

    if len(memory) == 0:
        print('EMPTY')
    else:
        print(f'{max(memory)} {min(memory)}')