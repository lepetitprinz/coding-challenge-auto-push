def solution(seoul):
    cnt = 0
    for name in seoul:
        if name == 'Kim':
            return f'김서방은 {cnt}에 있다'
        cnt += 1