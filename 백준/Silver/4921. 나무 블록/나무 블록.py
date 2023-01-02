import sys

input = lambda: sys.stdin.readline().rstrip()

seq_map = {
    "1": ["4", "5"], "3": ["4", "5"], "4": ["2", "3"], 
    "5": ["8"], "6": ["2", "3"], "7": ["8"], "8": ["6", "7"]
}

def check(seq):
    flag = False
    if seq[0] == "1" and seq[-1] == "2":
        if "1" not in seq[1: -1] and "2" not in seq[1: -1]:
            for i in range(len(seq) - 1):
                if seq[i + 1] not in seq_map[seq[i]]:
                    break
            else:
                flag = True
    
    return flag

cnt = 0
while True:
    seq = input()
    if seq == '0':
        break
    else:
        cnt += 1
        result = check(seq)
        if result:
            print(f"{cnt}. VALID")
        else:
            print(f"{cnt}. NOT")