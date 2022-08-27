import sys

test = int(input())
for _ in range(test):
    n = int(sys.stdin.readline())
    data = {}
    tot = 0
    for i in range(n):
        vote = int(sys.stdin.readline())
        tot += vote
        if vote in data:
            data[vote].append(i+1)
        else:
            data[vote] = [i+1]
    max_vote = max(data.keys())
    winners = data[max_vote]
    if len(winners) > 1:
        print('no winner')
    else:
        winner = winners[0]
        if max_vote > (tot/2):
            print(f'majority winner {winner}')
        else:
            print(f'minority winner {winner}')