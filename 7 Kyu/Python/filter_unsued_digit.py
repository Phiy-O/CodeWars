# [ 7 kyu ] Filter Unsued Digit
def unused_digits(*numbers):
    #your code here
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in numbers:
        for y in str(x):
            if y in arr:
                arr.remove(y)
            continue
    return ''.join(arr)
