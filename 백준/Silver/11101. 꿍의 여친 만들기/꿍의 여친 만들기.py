import sys

t = int(input())
for _ in range(t):
    # make ability hash map
    abilities = {}
    for ability_score in sys.stdin.readline().rstrip().split(','):
        ability, score = ability_score.split(':')
        abilities[ability] = int(score)
    
    min_time = 1000
    for cand_group in sys.stdin.readline().rstrip().split('|'):
        candidates = cand_group.split('&')
        time = max([abilities[cand] for cand in candidates])
        if time < min_time:
            min_time = time
    print(min_time)