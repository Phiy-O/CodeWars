def find_smallest(numbers, to_return):
    check = numbers[0]
    check_index = 0
    for x in range(len(numbers)):
        if numbers[x] < check:
            check = numbers[x]
            check_index = x
    if to_return == 'index':
        return check_index
    
    if to_return == 'value':
        return check
