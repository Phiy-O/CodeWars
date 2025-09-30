# [ 7 kyu ] Sum of array singles
def repeats(arr):
    new_arr = []
    for x in arr:
        if arr.count(x) == 1:
            new_arr.append(x)
    return sum(new_arr)
