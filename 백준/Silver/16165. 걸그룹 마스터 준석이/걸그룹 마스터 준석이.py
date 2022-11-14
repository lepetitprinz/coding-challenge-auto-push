import sys
input = lambda: sys.stdin.readline().rstrip()

def set_data(n):
    team = {}
    member = {}
    for _ in range(n):
        team_name = input()
        mem_len = int(input())
        team_list = []
        for _ in range(mem_len):
            m = input()
            team_list.append(m)
            member[m] = team_name
        team[team_name] = sorted(team_list)

    return team, member


def quiz(m, team, member):
    for _ in range(m):
        q = input()
        kind = int(input())
        if kind == 0:
            result = team[q]
            print(*result, sep='\n')
        else:
            result = member[q]
            print(result)


n, m = map(int, input().split())
team, member = set_data(n)
quiz(m, team, member)