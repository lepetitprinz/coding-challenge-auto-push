from math import ceil

def compare(data, n, length):
    nums_length = list(range(10 ** length, 10 ** (length + 1)))
    if length == 0:
        nums_length.append(0)
        nums_length = sorted(nums_length)

    result = -1
    data_of_length = set()
    for i in range(n - length):
        data_of_length.add(int(''.join(data[i: i + length+1])))
    for number in nums_length:
        if number not in data_of_length:
            result = number
            break

    return result


n = int(input())
data = []
for _ in range(ceil(n / 19)):
    data.extend(list(input().split()))

length = 0
while length < n + 1:
    result = compare(data, n, length)

    if result != -1:
        print(result)
        break
    else:
        length += 1