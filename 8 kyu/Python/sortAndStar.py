def two_sort(array):
    # your code here
    array.sort()
    arr = array[0]
    list_arr = list(arr)
    list_join = '***'.join(list_arr)
    return list_join
