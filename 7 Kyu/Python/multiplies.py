# [ 7 kyu ] Return the first M multiples of N
def multiples(m, n):
    # Implement me! :)
    arr = []
    for x in range(1, m + 1):
        arr.append(x * n)
    return arr
