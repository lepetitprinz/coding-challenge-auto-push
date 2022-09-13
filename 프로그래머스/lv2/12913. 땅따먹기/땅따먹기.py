def solution(land):
    
    answer = land[0]
    for l in land[1:]:
        row1 = max(answer[1:])
        row2 = max([answer[i] for i in [0,2,3]])
        row3 = max([answer[i] for i in [0,1,3]])
        row4 = max(answer[:-1])
        answer = [l[0] + row1, l[1] + row2, l[2] + row3, l[3] + row4]

    result = max(answer)

    return result