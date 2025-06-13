def print_array(arr):
    res = []
    for x in arr:
        str_arr = str(x)
        res.append(str_arr)
    return ','.join(res)
