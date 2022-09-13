def solution(board, moves):
    basket = []
    cnt = 0
    for move in moves:
        for line in board:
            if line[move-1] != 0:
                basket.append(line[move-1])
                line[move-1] = 0
                break
                
        if len(basket) >= 2:
            if basket[-2] == basket[-1]:
                cnt += 2
                basket = basket[:-2]

                    
    return cnt