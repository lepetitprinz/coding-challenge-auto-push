n, m = map(int, input().split())
data = list(map(int, input().split()))

mod_count = {}
cumsum = data[0]
mod_count[cumsum % m] = 1
for i in range(1, n):
    cumsum += data[i]
    mod = cumsum % m
    if mod in mod_count:
        mod_count[mod] += 1
    else:
        mod_count[mod] = 1

result = mod_count.get(0, 0)
for cnt in mod_count.values():
    result += cnt * (cnt -1) // 2

print(result)