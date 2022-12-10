raw_data = []
while True:
    try:
        raw_data.extend(input().split())
    except EOFError:
        break
        
n = int(raw_data[0])
data = raw_data[1:]

rev_data = sorted([int(str_num[::-1]) for str_num in data])
print(*rev_data, sep='\n')