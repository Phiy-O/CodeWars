def remove_every_other(my_list):
    arr = []
    for x in range(len(my_list)):
        if x % 2 == 0:
            arr.append(my_list[x])
    return arr
