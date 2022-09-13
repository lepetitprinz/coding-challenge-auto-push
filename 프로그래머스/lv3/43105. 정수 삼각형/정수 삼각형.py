def solution(triangle):
    d = [0] * 500
    d[0] = triangle[0]
    for i, values in enumerate(triangle):
        if i != 0:
            d_depth = []
            for j in range(i+1):
                if j == 0:
                    d_depth.append(d[i-1][0] + values[0])
                elif j == i:
                    d_depth.append(d[i-1][-1] + values[-1])
                else:
                    d_depth.append(max(d[i-1][j-1], d[i-1][j]) + values[j])
            d[i] = d_depth

    return max(d[len(triangle)-1])