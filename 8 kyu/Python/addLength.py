def add_length(str_):
    #your code here
    arr = []
    n = str_.split()
    for x in range(len(n)):
        y = f"{n[x]} {len(n[x])}"
        arr.append(y)
    return arr
