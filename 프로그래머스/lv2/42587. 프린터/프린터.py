from collections import deque

def solution(priorities, location):
    queue_list = [(i, p) for i, p in enumerate(priorities)]
    queue = deque(queue_list)

    order = []
    while len(queue) > 0:
        cur = queue.popleft()
        if queue:
            if any(cur[1] < q[1] for q in queue):
                queue.append(cur)
            else:
                order.append(cur[0])
        else:
            order.append(cur[0])

    return order.index(location) + 1