# [ 7 kyu ] Decreasing Input
def add(*args):
    arr = []
    result = 0
    if len(args) == 0:
        return 0
    
    for x in range(1, len(args) + 1):
        arr.append(args[x - 1] / x)
        result += arr[x - 1]
    return round(result)
