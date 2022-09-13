from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_queue = deque(truck_weights)
    bridge_on = deque([0] * bridge_length)
    bridge_weight = 0
    while True:
        if len(truck_queue) == 0 and len(bridge_on) == 0:
            break
        truck_left = bridge_on.popleft() 
        bridge_weight -= truck_left
        if len(truck_queue) != 0:
            if bridge_weight + truck_queue[0] <= weight:
                truck_move = truck_queue.popleft()
                bridge_on.append(truck_move)
                bridge_weight += truck_move
            else:
                bridge_on.append(0)
        answer += 1
    
    return answer