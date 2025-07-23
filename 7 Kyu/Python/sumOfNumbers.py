def show_sequence(n):
    res = 0
    arr = []
    for x in range(0, n + 1):
        res += x
        arr.append(str(x))
    
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return f"{n}=0"
    else:
        return f"{'+'.join(arr)} = {res}"
