def solution(numbers):
    total = sum(list(range(0, 10)))
    answer = total - sum(numbers)
    return answer