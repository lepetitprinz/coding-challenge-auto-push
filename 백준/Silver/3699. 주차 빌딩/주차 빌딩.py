import sys
from collections import deque


def get_seq_order(row):
    order = []
    for number in row:
        if number != -1:
            order.append(number)

    return sorted(order)


def rotation(queue, num, l):
    idx = queue.index(num)
    if idx < l / 2:
        move = idx
        for _ in range(move):
            queue.rotate(-1)
    else:
        move = l - idx
        for _ in range(move):
            queue.rotate()
    duration = move * 5

    return queue, duration


t = int(input())
for _ in range(t):
    h, l = map(int, input().split())

    result = 0
    for i in range(h):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        seq = get_seq_order(row=row)
        result += len(seq) * 20 * i
        queue = deque(row)

        for num in seq:
            queue, duration = rotation(queue, num, l)
            result += duration

    print(result)