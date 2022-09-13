def get_dist(l1, l2):
    dist = 0
    dist += abs(l1[0] - l2[0])
    dist += abs(l1[1] - l2[1])
    
    return dist

def solution(numbers, hand):
    loc_map = {
        1: [0, 3], 2: [1, 3], 3: [2, 3],
        4: [0, 2], 5: [1, 2], 6: [2, 2],
        7: [0, 1], 8: [1, 1], 9: [2, 1],
        '*': [0, 0], 0: [1, 0], '#': [2, 0]
    }
    
    l_hand = loc_map['*']
    r_hand = loc_map['#']
    l_dist = 0
    r_dist = 0
    
    result = []
    for num in numbers:
        if num in [1, 4, 7]:
            result.append('L')
            l_hand = loc_map[num]
        elif num in [3, 6, 9]:
            result.append('R')
            r_hand = loc_map[num]
        else:
            l_dist = get_dist(l_hand, loc_map[num])
            r_dist = get_dist(r_hand, loc_map[num])
            if l_dist < r_dist:
                result.append('L')
                l_hand = loc_map[num]
            elif l_dist > r_dist:
                result.append('R')
                r_hand = loc_map[num]
            else:
                if hand == 'right':
                    result.append('R')
                    r_hand = loc_map[num]
                else:
                    result.append('L')
                    l_hand = loc_map[num]

    return ''.join(result)