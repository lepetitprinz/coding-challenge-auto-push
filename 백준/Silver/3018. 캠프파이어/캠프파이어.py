import sys

n = int(input())
e = int(input())
tot_song = []

data = {i: set() for i in range(1, n + 1)}
for song in range(e):
    people = set(list(map(int, sys.stdin.readline().split()))[1:])
    if 1 in people:
        tot_song.append(song)
        for p in people:
            data[p].add(song)
    else:
        total = set()
        for s in data.values():
            total = total | s
        for p in people:
            data[p] = total.copy()

length = len(tot_song)
for p, song in data.items():
    if len(song) == length:
        print(p)