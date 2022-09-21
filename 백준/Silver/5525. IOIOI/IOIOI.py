def kmp(string, pattern):
    table = [0 for _ in range(len(pattern))]
    
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
        
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
            
    count = 0
    i = 0
    for j in range(len(string)):
        while i > 0 and pattern[i] != string[j]:
            i = table[i-1]
        
        if pattern[i] == string[j]:
            i += 1
            if i == len(pattern):
                count += 1
                i = table[i-1]

    return count
    
n = int(input())
m = int(input())
string = input()

pattern = ''.join(['I'] + ['OI'] * n)
print(kmp(string, pattern))