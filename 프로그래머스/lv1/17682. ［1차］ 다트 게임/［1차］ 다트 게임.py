number = [str(i) for i in range(10)]
bonus = ['S', 'D', 'T']
option = ['*', '#']

def split_score(result):
    length = len(result)
    scores = []
    temp = ''
    for i, value in enumerate(result):
        if value in number:
            temp += value
        elif value in bonus:
            if i != length-1:
                if result[i+1] not in option:
                    temp += value
                    scores.append(temp)
                    temp = ''
                else:
                    temp += value
            else:
                temp += value
                scores.append(temp)
        elif value in option:
            temp += value
            scores.append(temp)
            temp = ''

    return scores

def calc_score(value):
    score = ''
    b = ''
    option = []
    for v in value:
        if v in number:
            score += v
        elif v in bonus:
            b += v

    score = int(score)

    if b == 'D':
        score = score ** 2
    elif b == 'T':
        score = score ** 3

    return score

def get_option(scores):
    options = []
    for score in scores:
        if '*' in score:
            options.append('*')
        elif '#' in score:
            options.append('#')
        else:
            options.append('')

    return options

def update_score(scores, options):
    result = []
    for i, (score, option) in enumerate(zip(scores, options)):
        if option == '#':
            score = score * (-1)
            result.append(score)
        elif option == '*':
            if i == 0:
                score = score * 2
                result.append(score)
            else:
                score = score * 2
                result[-1] = result[-1] * 2
                result.append(score)
        else:
            result.append(score)

    return sum(result)

def solution(dartResult):
    score_list = split_score(dartResult)
    scores = [calc_score(score) for score in score_list]
    options = get_option(score_list)

    answer = update_score(scores, options)
    
    return answer