import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

queue = []
order_time = {}
for _ in range(n):
    order = input().split()
    if order[0] == "order":
        table = int(order[1])
        time = int(order[2])
        queue.append(table)
        order_time[table] = time
    elif order[0] == "sort":
        queue = sorted(queue, key=lambda x: (order_time[x], x))
    else:
        table = int(order[1])
        queue.remove(table)
        
    if len(queue) > 0:
        print(*queue)
    else:
        print("sleep")