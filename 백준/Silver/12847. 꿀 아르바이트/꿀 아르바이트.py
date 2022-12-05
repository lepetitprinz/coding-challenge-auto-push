n, m = map(int, input().split())
data = list(map(int, input().split()))

slide_sum = sum(data[:m])
max_sum = slide_sum

for s, e in zip(data[:n - m], data[m:]):
    slide_sum = slide_sum - s + e
    if slide_sum > max_sum:
        max_sum = slide_sum
        
print(max_sum)