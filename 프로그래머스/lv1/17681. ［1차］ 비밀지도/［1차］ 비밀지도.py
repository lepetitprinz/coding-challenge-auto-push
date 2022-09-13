def solution(n, arr1, arr2):
    nums = [2**i for i in range(n-1, -1, -1)]
    
    mat1 = []
    for num in arr1:
        temp = []
        for divisor in nums:
            if num % divisor != num:
                temp.append("#")
                num = num % divisor
            else:
                temp.append("@")
        mat1.append(temp)
        
    mat2 = []
    for num in arr2:
        temp = []
        for divisor in nums:
            if num % divisor != num:
                temp.append("#")
                num = num % divisor
            else:
                temp.append("@")
        mat2.append(temp) 
    
    result = []
    for l1, l2 in zip(mat1, mat2):
        temp = []
        for s1, s2 in zip(l1, l2):
            if (s1 == '@') and (s2 == '@'):
                temp.append(" ")
            else:
                temp.append("#")
        temp = ''.join(temp)
        result.append(temp)

    return result