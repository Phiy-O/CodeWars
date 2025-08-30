# [ 7 kyu ] Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    #good luck!
    if a == b:
        return a
    result = 0
    
    if a < b:
        for x in range(a, b + 1):
            result += x
    else:
        for y in range(b, a + 1):
            result += y
    return result
