import sys

input = lambda: sys.stdin.readline().rstrip()

while True:
    try:
        record = []
        n = int(input())
        for _ in range(n):
            data = set(list(input()))
            if data not in record:
                record.append(data)
        print(len(record))

    except:
        break