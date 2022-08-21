import sys

while True:
    page = int(sys.stdin.readline().rstrip())
    if page == 0:
        break
    
    requests = list(sys.stdin.readline().rstrip().split(','))
    result = set()
    for request in requests:
        r = request.split('-')
        if len(r) == 1:
            if int(r[0]) <= page:
                result.add(int(r[0]))
        else:
            result = result | set(range(int(r[0]), min(int(r[1]) + 1, page + 1)))
    
    print(len(result))