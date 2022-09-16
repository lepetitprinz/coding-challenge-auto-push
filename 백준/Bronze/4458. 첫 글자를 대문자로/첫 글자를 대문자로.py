import sys

t = int(input())
for _ in range(t):
    sentence = sys.stdin.readline().rstrip()
    print(sentence[0].upper() + sentence[1:])