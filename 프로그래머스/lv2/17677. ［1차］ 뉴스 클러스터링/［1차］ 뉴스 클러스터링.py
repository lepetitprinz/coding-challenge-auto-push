from collections import Counter

def solution(str1, str2):
    cnt1 = make_jaccard_count(str1)
    cnt2 = make_jaccard_count(str2)
    
    result = calc_jaccard_similarity(cnt1, cnt2)
    
    return result

def make_jaccard_count(string):
    string = string.lower()
    
    jaccard_list = []
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            jaccard_list.append(string[i] + string[i+1])
    jaccard_cnt = dict(Counter(jaccard_list))    
        
    return jaccard_cnt

def calc_jaccard_similarity(cnt1, cnt2):
    all_key = list(set(cnt1).union(set(cnt2)))
    
    union = 0
    intersection = 0
    for key in all_key:
        c1 = cnt1.get(key, 0)
        c2 = cnt2.get(key, 0)
        union += max(c1, c2)
        intersection += min(c1, c2)
    
    if union == 0:
        result = 1
    else:
        result = intersection / union
        
    return int(result * 65536)