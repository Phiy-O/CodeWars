def distinct(seq):
    arr = []
    
    for x in seq:
        if x not in arr:
            arr.append(x)
    return arr
