from string import ascii_uppercase


def solution(msg):
    dictionary = {word: i + 1 for i, word in enumerate(ascii_uppercase)}

    dict_idx = 26
    idx = 0
    length = len(msg)
    answer = []
    while idx < length:
        for i in range(1, length - idx + 1):
            if msg[idx: idx + i] not in dictionary:
                answer.append(dictionary[msg[idx: idx + i - 1]])
                dict_idx += 1
                dictionary[msg[idx: idx + i]] = dict_idx
                idx += i - 1
                break

            if idx + i == length:
                answer.append(dictionary.get(msg[idx: idx + i], dict_idx+1))
                idx += i
                break

    return answer