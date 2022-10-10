alpha = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2, 'K': 2,
    'L': 1, 'M': 2, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1,
    'W': 1, 'X': 2, 'Y': 2, 'Z': 1,
}


def dp(seq):
    length = len(seq)

    d = []
    for i in range(length, 0, -1):
        d.append([0] * i)

    d[0] = [alpha[s] for s in seq]

    for i in range(1, length - 1):
        for j in range(length - i):
            d[i][j] = (d[i - 1][j] + d[i - 1][j + 1]) % 10

    return d[length-2]


he = input()
she = input()
seq = []
for h, s in zip(he, she):
    seq.extend([h, s])

result = dp(seq)
print(''.join(map(str, result)))