import sys

input = lambda: sys.stdin.readline().rstrip()

def search_next_rectangle(h, w):
    diagonal = h ** 2 + w ** 2
    result = search_same_length(w, diagonal)
    if not result:
        result = search_larger_rectangle(diagonal)

    return result


def search_same_length(w, diagonal):
    for i in range(1, w):
        for j in range(1, w):
            if i < j:
                length = i ** 2 + j ** 2
                if length == diagonal:
                    return i, j
                elif length > diagonal:
                    break

    return False


def search_larger_rectangle(diagonal):
    while True:
        diagonal += 1
        max_val = int(diagonal ** 0.5) + 2
        for i in range(1, max_val):
            for j in range(1, max_val):
                if i < j:
                    length = i ** 2 + j ** 2
                    if length == diagonal:
                        return i, j
                    elif length > diagonal:
                        break


while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    else:
        result = search_next_rectangle(h, w)
        print(*result)