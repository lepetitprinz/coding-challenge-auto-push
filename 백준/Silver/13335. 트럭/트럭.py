from collections import deque

def update_remain_distance(queue):
    new_queue = deque()
    while queue:
        weight, remain_distance = queue.popleft()
        new_queue.append([weight, remain_distance - 1])

    return new_queue


n, length, max_weight = map(int, input().split())
trucks = deque(map(int, input().split()))
weight = trucks.popleft()
queue = deque([[weight, length]])

time = 1
curr_weight = weight
while queue:
    queue = update_remain_distance(queue)
    while queue:
        weight, remain_distance = queue.popleft()
        if remain_distance == 0:
            curr_weight -= weight
        else:
            queue.appendleft([weight, remain_distance])
            break

    if len(trucks) > 0:
        new_weight = trucks.popleft()
        if curr_weight + new_weight <= max_weight:
            queue.append([new_weight, length])
            curr_weight += new_weight
        else:
            trucks.appendleft(new_weight)

    time += 1

print(time)