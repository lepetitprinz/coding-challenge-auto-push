def rule(word):
    upper = sum(char.isupper() for char in word)
    kinds = ''.join(sorted(list(word.lower())))
    
    return upper, kinds

def combination(n):
    return n * (n - 1) // 2

test = int(input())
for _ in range(test):
    n, k = map(int, input().split())
    data = list(input().split())    
    
    cnt = {}
    for word in data:
        upper, kinds = rule(word)
        if (upper, kinds) in cnt:
            cnt[(upper, kinds)] += 1
        else:
            cnt[(upper, kinds)] = 1
            
    result = sum(combination(i) for i in cnt.values())   
    print(result)