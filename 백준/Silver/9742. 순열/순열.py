import sys
from math import factorial

while True:
    try:
        word, k = sys.stdin.readline().rstrip().split()
        k = int(k)
        length = len(word)
        if k > factorial(length):
            print(f'{word} {k} = No permutation')
        else:
            w = word
            n = k - 1
            result = []
            for i in range(1, length + 1):
                loc = n // factorial(length - i)
                n = n % factorial(length - i)
                result.append(w[loc])
                w = w[:loc] + w[loc + 1:]
            print(f"{word} {k} = {''.join(result)}")
    except:
          break