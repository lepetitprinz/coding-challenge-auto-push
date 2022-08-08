def command(action, value, location, direction):
    if action == 'TURN':
        direction = dir_change[value][direction]
    elif action == 'MOVE':
        location[0] += dir_map[direction][0] * value
        location[1] += dir_map[direction][1] * value
    
    return location, direction

dir_map = {'right': [1, 0], 'left': [-1 ,0], 'up': [0, 1], 'down': [0, -1]}
dir_change = {
    0: {'right': 'up', 'left': 'down', 'up': 'left', 'down': 'right'},
    1: {'right': 'down', 'left': 'up', 'up': 'right', 'down': 'left'}
}
m, n = map(int, input().split())
location = [0, 0]
direction = 'right'

for _ in range(n):
    action, value = input().split()
    location, direction = command(action, int(value), location, direction)
    
    if (location[0] <0) or (location[0] > m) or (location[1] < 0) or (location[1] > m):
        location = [-1]
        break

print(*location)