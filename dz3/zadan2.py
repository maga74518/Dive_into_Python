dict1 = {1: '1', '2': 2, (3, ): [3], 4: set([4, 5, 7])}
dict2 = {}

for i in dict1.items():
    try:
        hash(i[1])
    except TypeError:
        dict2[f'{i[1]}'] = i[0]
    else:
        dict2[i[1]] = i[0]
print(dict2)