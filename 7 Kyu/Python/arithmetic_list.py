# [ 7 kyu ] Arithmetic List
def seqlist(first, c, l):
    arr = []
    while True:
        arr.append(first)
        first += c
        if len(arr) == l:
            break
        
    return arr
