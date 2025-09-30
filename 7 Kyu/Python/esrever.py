# [ 7 kyu ] esreveR
def reverse(lst):
    empty_list = list()          # use this!
    for x in range(len(lst) - 1, -1, -1):
        empty_list.append(lst[x])
    return empty_list
