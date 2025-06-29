def ordered_count(inp):
    arr = []
    for x in range(len(list(inp))):
        if (list(inp)[x], inp.count(list(inp)[x])) not in arr :
            arr.append((list(inp)[x], inp.count(list(inp)[x])))
    return arr
