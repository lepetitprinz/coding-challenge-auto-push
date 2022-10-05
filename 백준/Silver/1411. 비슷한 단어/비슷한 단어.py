import sys

input = lambda: sys.stdin.readline().rstrip()

def combination(n):
    return n * (n - 1) // 2


def get_rule(word):
    history = {}
    seq = 0
    rule = []
    for char in word:
        if char in history:
            rule.append(history[char])
        else:
            seq += 1
            rule.append(str(seq))
            history[char] = str(seq)

    return ''.join(rule)


n = int(input())
cnt = {}
for _ in range(n):
    word = input()
    rule = get_rule(word)
    if rule in cnt:
        cnt[rule] += 1
    else:
        cnt[rule] = 1

result = sum(combination(i) for i in cnt.values())
print(result)