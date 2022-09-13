def solution(clothes):
    cloth_dict = dict()
    for name, kind in clothes:
        try:
            cnt = cloth_dict[kind]
            cloth_dict[kind] = cnt + 1
        except:
            cloth_dict[kind] = 1

    answer = 1
    for val in cloth_dict.values():
        answer = answer * (val+1)
    
    return answer - 1