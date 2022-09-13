def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    cnt = 0
    zeros = 0
    for number in lottos:
        if number in win_nums:
            cnt += 1
        elif number == 0:
            zeros += 1
    
    rank_min = rank.get(cnt, 6)
    rank_max = rank.get(cnt+zeros, 6)
    
    answer = [rank_max, rank_min]
    
    return answer