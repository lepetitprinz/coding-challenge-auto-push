import sys

loc = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 
    'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 
    'k': (1, 7), 'l': (1, 8),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)
}

def compare_word(word1, word2):
    distance = 0
    for alpha1, alpha2 in zip(word1, word2):
        distance += cal_manhattan_distance(alpha1, alpha2)
    
    return distance

def cal_manhattan_distance(alpha1, alpha2):
    x1, y1 = loc[alpha1]
    x2, y2 = loc[alpha2]
    
    return abs(x2 - x1) + abs(y2 - y1)

test = int(input())
for _ in range(test):
    w, l = sys.stdin.readline().rstrip().split()
    
    dist = []
    for _ in range(int(l)):
        word = sys.stdin.readline().rstrip()
        dist.append([word, compare_word(w, word)])
    result = sorted(dist, key=lambda x: (x[1], x[0]))
    for r in result:
        print(*r)