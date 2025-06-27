def dont_give_me_five(start,end):
    # your code here
    arr = []
    for x in range(start, end + 1):
        if '5' not in str(x):
            arr.append(x) # amount of numbers
    return len(arr)
