def solution(prices):
    answer = []
    len_prices = len(prices)

    for i in range(len_prices):
        val = prices[i]
        cnt = 0
        for j in range(i+1, len_prices):
            if val <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    return answer