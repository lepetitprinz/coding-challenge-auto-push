def solution(absolutes, signs):
    bool_map = {True: 1, False: -1}
    signs = [bool_map[b] for b in signs]
    
    result = [x*y for x, y in zip(absolutes, signs)]

    return sum(result)