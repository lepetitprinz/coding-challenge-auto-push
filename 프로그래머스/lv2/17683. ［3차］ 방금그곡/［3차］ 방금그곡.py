import datetime as dt

conv_map = {'C': 'a', 'C#': 'b', 'D': 'c', 'D#': 'd', 'E': 'e', 'F': 'f', 'F#': 'g', 
            'G': 'h', 'G#': 'i', 'A': 'j', 'A#': 'k', 'B': 'l', 'E#': 'n'}

def convert(string):
    length = len(string)
    
    result = ''
    for i in range(length):
        if i < length-1:
            if string[i+1] == '#':
                result += conv_map[string[i:i+2]]
            else:
                result += conv_map.get(string[i], '')
        else:
            result += conv_map.get(string[i], '')
        
    return result

def make_melody(music_info):
    music_info = music_info.split(',')
    music_info[3] = convert(music_info[3])
    
    start_h, start_m = map(int, music_info[0].split(':'))
    end_h, end_m = map(int, music_info[1].split(':'))
    
    start_time = dt.timedelta(hours=start_h, minutes=start_m)
    end_time = dt.timedelta(hours=end_h, minutes=end_m)
    duration = (end_time - start_time) / dt.timedelta(seconds=60)
    
    mod = int(duration//len(music_info[3]))
    remain = int(duration % len(music_info[3]))
    melody = music_info[3] * mod + music_info[3][: remain]

    return [music_info[2], melody, duration]

def solution(m, musicinfos):
    m = convert(m)
    
    result_list = []
    for music_info in musicinfos:
        info = make_melody(music_info)
        if m in info[1]:
            result_list.append(info)
    
    if len(result_list) == 0:
        result = '(None)'
        
    elif len(result_list) == 1:
        result = result_list[0][0]
        
    else:
        result = sorted(result_list, key=lambda x: x[2], reverse=True)[0][0]
    
    return result