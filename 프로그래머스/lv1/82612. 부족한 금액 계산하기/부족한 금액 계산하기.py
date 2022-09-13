def solution(price, money, count):
    cnt_sum = sum(list(range(1, count+1)))
    total = price * cnt_sum
    result = total - money
    
    if result <=0:
        answer = 0
    else:
        answer = result

    return answer