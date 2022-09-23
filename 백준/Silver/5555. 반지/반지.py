search = input()
length = len(search)

count = 0
for _ in range(int(input())):
    string = input()
    s_len = len(string)
    for i in range(s_len):
        end = i + length
        if end <= s_len:
            comp = string[i: end]
        else:
            comp = string[i: ] + string[: end - s_len]
        if comp == search:
            count += 1
            break

print(count)