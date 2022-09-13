def get_number(n):
    if n % 4 == 3:
        n_bin = bin(n)[2:]
        n_bin = n_bin.zfill(len(n_bin) + 1)
        for i in range(len(n_bin)-1, -1, -1):
            if n_bin[i] == '0':
                answer = int(n_bin[:i] + '10' + n_bin[i+2:], 2)
                break
    else:
        answer = n + 1
    
    return answer

def solution(numbers):
    result = [get_number(number) for number in numbers]
    
    return result