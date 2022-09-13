comment = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

def solution(record):
    record_hist = []
    id_nick_map = {}

    for rec in record:
        rec = rec.split(" ")
        if rec[0] in ['Enter', 'Change']:
            id_nick_map[rec[1]] = rec[2]

        record_hist.append([rec[1], rec[0]])

    answer = [id_nick_map[id] + comment[action] for id, action in record_hist if action != 'Change']
    
    return answer