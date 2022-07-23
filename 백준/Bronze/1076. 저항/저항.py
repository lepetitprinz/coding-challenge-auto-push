hash_map = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 
    'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

n1 = str(hash_map[input()])
n2 = str(hash_map[input()])
multiple = hash_map[input()]
print(int(n1 + n2) * 10 ** multiple)