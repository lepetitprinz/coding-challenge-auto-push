n = int(input())
answers = list(map(int, input().split()))

print(sum(1 for ans in answers if ans == n))