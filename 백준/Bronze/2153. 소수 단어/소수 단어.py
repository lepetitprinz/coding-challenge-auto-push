from string import ascii_lowercase, ascii_uppercase

def is_prime(num):
    result = ''
    if num % 2 == 0:
        if num > 2:
            result = 'not '
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                if num > i:
                    result = 'not '
                break
                    
    return result

alphabets = {alpha:i+1 for i, alpha in enumerate(ascii_lowercase+ascii_uppercase)}

sum_word = sum(alphabets[w] for w in input())
print(f'It is {is_prime(sum_word)}a prime word.')