def remove_duplicates(l):
    new_l = []

    for num in l:
        if num not in new_l:
            new_l.append(num)
    return new_l





l = [1,2,3,4,3,3,2,4,6,5]

print(remove_duplicates(l))