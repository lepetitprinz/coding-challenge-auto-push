from collections import deque

def revise_skill_tree(skill, skill_trees):
    skill_trees_revised = []
    for skill_tree in skill_trees:
        tree = ''
        for s in skill_tree:
            if s in skill:
                tree += s
        skill_trees_revised.append(tree)

    return skill_trees_revised


def solution(skill, skill_trees):
    skill_trees_revised = revise_skill_tree(skill, skill_trees)

    cnt = 0
    for skill_tree in skill_trees_revised:
        queue = deque(list(skill[:]))
        while queue:
            for s in skill_tree:
                if queue.popleft() == s:
                    continue
                else:
                    cnt -= 1
                    break
            cnt += 1
            break

    return cnt