import numpy as np

def solution(progresses, speeds):
    queue = np.array(progresses)
    speeds = np.array(speeds)

    answer = []
    while len(queue) > 0:
        queue += speeds
        deploy = 0
        while len(queue) > 0:
            progress = queue[0]
            if progress >= 100:
                deploy += 1
                queue = np.delete(queue, 0)
                speeds = np.delete(speeds, 0)
            else:
                break
        if deploy > 0:
            answer.append(deploy)

    return answer