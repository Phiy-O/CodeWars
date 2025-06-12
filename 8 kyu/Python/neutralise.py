def neutralise(s1, s2):
    arr = []
    
    for x in range(len(s1)):
        arr.append(s1[x] + s2[x])
        if "++" in arr:
            arr[x] = "+"
        elif "--" in arr:
            arr[x] = "-"
        else:
            arr[x] = "0"
    return ''.join(arr)
