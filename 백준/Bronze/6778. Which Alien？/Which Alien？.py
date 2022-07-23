def condition(antenna, eyes):
    result = []
    if (antenna >=3) and (eyes <= 4):
        result.append('TroyMartian')
    if (antenna <=6) and (eyes >= 2):
        result.append('VladSaturnian')
    if (antenna <=2) and (eyes <= 3):
        result.append('GraemeMercurian')
        
    return result

antenna = int(input())
eyes = int(input())
result = condition(antenna, eyes)
if len(result) != 0:
    for r in result:
        print(r)