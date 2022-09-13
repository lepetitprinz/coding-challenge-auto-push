def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]

    cashe = []
    time = 0
    for city in cities:
        if city in cashe:
            time += 1
            cashe.pop(cashe.index(city))
            cashe.append(city)
        else:
            time += 5
            if cacheSize == 0:
                cashe = []
            else:
                cashe.append(city)
                if len(cashe) > cacheSize:
                    cashe.pop(0)

    return time