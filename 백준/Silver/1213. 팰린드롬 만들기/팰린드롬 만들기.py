def is_palindrome(str_cnt, length):
    flag = True
    if length % 2 == 0:
        for cnt in str_cnt.values():
            if cnt % 2 == 1:
                flag = False
                break
    else:
        odd_cnt = 0
        for cnt in str_cnt.values():
            if cnt % 2 == 1:
                odd_cnt += 1
            if odd_cnt > 1:
                flag = False
                break
    
    return flag

def make_palindrome(str_cnt, length):
    palindrome = []
    if length % 2 == 0:
        for s, cnt in str_cnt.items():
            palindrome.extend([s] * (cnt // 2))

        palindrome = palindrome + palindrome[::-1]
    else:
        middle = []
        for s, cnt in str_cnt.items():
            if cnt % 2 == 0:
                palindrome.extend([s] * (cnt // 2))
            else:
                palindrome.extend([s] * (cnt // 2))
                middle.append(s)
        palindrome = palindrome + middle + palindrome[::-1]
    
    return ''.join(palindrome)
    

str_list = sorted(list(input()))
length = len(str_list)
str_cnt = {}
for s in str_list:
    if s in str_cnt:
        str_cnt[s] += 1
    else:
        str_cnt[s] = 1

if is_palindrome(str_cnt, length):
    palindrome = make_palindrome(str_cnt, length)
    print(palindrome)
else:
    print("I'm Sorry Hansoo")