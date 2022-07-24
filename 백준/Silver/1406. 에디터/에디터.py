from __future__ import annotations
from typing import Any

class Node:
    def __init__(self, prev: Node = None, next: Node = None, data: Any = None):
        self.prev = prev
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def insert(self, data):
        if self.current is None:
            self.head = Node(None, None, data)
            self.current = self.head
        else:
            nxt = self.current.next
            self.current.next = Node(self.current, nxt, data)
            if nxt is not None:
                nxt.prev = self.current.next
            if self.current == self.head:
                self.head.next = self.current.next
            self.current = self.current.next

    def delete(self):
        if self.current == self.head:
            self.head = self.current.next
            self.current.next.prev = self.current.prev
        else:
            if self.current.next is not None:
                self.current.next.prev = self.current.prev
            self.current.prev.next = self.current.next
            self.current = self.current.prev

    def move_left(self):
        self.current = self.current.prev

    def move_right(self):
        self.current = self.current.next


if __name__ =='__main__':
    ls = LinkedList()
    ls.insert('start')
    s = input()
    for ss in s:
        ls.insert(ss)

    n = int(input())
    for _ in range(n):
        inp = input().split()
        cmd = inp[0]
        if cmd == 'L':
            if ls.current.prev is not None:
                ls.move_left()
        elif cmd == 'D':
            if ls.current.next is not None:
                ls.move_right()
        elif cmd == 'B':
            if ls.current is not None and ls.current.prev is not None:
                ls.delete()
        elif cmd == 'P':
            ls.insert(inp[1])

    prt = ls.head.next
    while prt:
        print(prt.data, end='')
        prt = prt.next