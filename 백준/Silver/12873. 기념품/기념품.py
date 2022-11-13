def queue(people):
    t = 1
    length = len(people)

    while length > 1:
        move = (t ** 3) % length
        if move != 0:
            people = people[move:] + people[:move - 1]
        else:
            people.pop()
        length -= 1
        t += 1

    return people[0]


n = int(input())
people = [i + 1 for i in range(n)]
result = queue(people)

print(result)