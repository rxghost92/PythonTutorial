lists = [1, 3, 8, 8, 4, 1, 0]
uniques = []

for list in lists:
    if list not in uniques:
        uniques.append(list)
        uniques.sort()


print(uniques)