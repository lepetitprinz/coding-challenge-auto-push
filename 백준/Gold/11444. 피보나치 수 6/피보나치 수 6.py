def fibonacci(n):
    base = [[1,1],[1,0]]
    if n == 1:
        matrix = base
    else:
        div_matrix = fibonacci(n // 2)
        matrix = [
                    [
                        (div_matrix[0][0] * div_matrix[0][0] + div_matrix[0][1] * div_matrix[1][0]) % 1000000007, 
                        (div_matrix[0][0] * div_matrix[0][1] + div_matrix[0][1] * div_matrix[1][1]) % 1000000007
                    ],
                    [
                        (div_matrix[1][0] * div_matrix[0][0] + div_matrix[1][1] * div_matrix[1][0]) % 1000000007, 
                        (div_matrix[1][0] * div_matrix[0][1] + div_matrix[1][1] * div_matrix[1][1]) % 1000000007
                    ]
        ]
        if n % 2 == 1:
            matrix = [
                        [
                            (matrix[0][0] * base[0][0] + matrix[0][1] * base[1][0]) % 1000000007, 
                            (matrix[0][0] * base[0][1] + matrix[0][1] * base[1][1]) % 1000000007
                        ],
                        [
                            (matrix[1][0] * base[0][0] + matrix[1][1] * base[1][0]) % 1000000007, 
                            (matrix[1][0] * base[0][1] + matrix[1][1] * base[1][1]) % 1000000007
                        ]
                    ]
    return matrix

n = int(input())
print(fibonacci(n)[0][1] % 1000000007)
