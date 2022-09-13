def solution(s):
    length = len(s)
    idx = length//2
    if length % 2 == 0:
        return s[idx- 1: idx + 1]
    else:
        return s[idx]