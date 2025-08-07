# [ 7 kyu ] Sum Even Number
def sum_even_numbers(seq): 
    # your code here
    if len(seq) == 0:
        return 0
    
    result = 0
    for x in seq:
        if x % 2 == 0:
            result += x
    return result
