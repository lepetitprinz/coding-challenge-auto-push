def solution(citations):
    citations = sorted(citations, reverse=True)
    
    for i in range(len(citations), 1, -1):
        cnt = 0
        for j in citations:
            if i <= j:
                cnt += 1
                if i == cnt:
                    return cnt
            else:
                break
                
    return 0