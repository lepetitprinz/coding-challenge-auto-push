import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        value = queue.popleft()

        for i in graph[value]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    return visited

def cycle_word(word):
    cycle = set()
    for i in range(len(word)):
        cycle.add(word[i:] + word[:i])

    return cycle

n = int(input())
words = []
words_cycle = {}
visited = {}
for _ in range(n):
    word = input()
    words.append(word)
    visited[word] = False
    words_cycle[word] = cycle_word(word)

graph = {}
for w1 in words:
    for w2 in words:
        if w1 != w2:
            if w2 in words_cycle[w1]:
                if w1 not in graph:
                    graph[w1] = [w2]
                else:
                    graph[w1].append(w2)
                    
    if w1 not in graph:
        graph[w1] = []

count = 0
for word in words:
    if not visited[word]:
        count += 1
        visited = bfs(graph, word, visited)

print(count)