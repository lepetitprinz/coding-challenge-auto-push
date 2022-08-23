import sys

def solution(string, length):
    result = 1
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            if kmp(string, length, i):
                result = length // i
                break

    return result

def kmp(string, length, width):
    flag = True
    s = string[:width]
    for j in range(0, length, width):
        if not string[j: j + width] == s:
            flag = False
            break

    return flag

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break

    length = len(string)
    result = solution(string, length)

    print(result)