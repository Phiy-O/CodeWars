# [ 7 kyu ] Flatten and sort an array
def flatten_and_sort(array):
    result = []
    
    for x in array:
        for y in x:
            result.append(y)
    return sorted(result)
