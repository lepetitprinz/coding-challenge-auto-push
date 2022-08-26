t = int(input())
for _ in range(t):
    word, c = input().split()
    c_len = len(c)

    time = 0
    idx = 0
    while idx < len(word):
        if word[idx] == c[0]:
            if word[idx: idx + c_len] == c:
                idx += c_len
                time += 1
            else:
                idx += 1
                time += 1
        else:
            idx += 1
            time += 1
    print(time)