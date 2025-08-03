# [ 7 kyu ] Find Factors Down to Limit
def factors(integer, limit):
    return [[] if limit > integer else num for num in range(limit, integer + 1) if integer % num == 0]
