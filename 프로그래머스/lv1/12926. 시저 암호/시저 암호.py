from string import ascii_lowercase

alphabet = ascii_lowercase
alpha_idx = {alpha: i for i, alpha in enumerate(alphabet)}

def string_converter(alpha, n):
    result = None
    if alpha == ' ':
        result = ' '
    else:
        idx = (alpha_idx[alpha.lower()] + n) % 26
        temp = alphabet[idx]

        if alpha.islower():
            result = temp
        else:
            result = temp.upper()

    return result


def solution(s, n):
    results = []
    for alpha in s:
        results.append(string_converter(alpha=alpha, n=n))

    answer = ''.join(results)
    
    return answer