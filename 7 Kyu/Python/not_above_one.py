# [ 7 kyu ] Not Above One
def binary_cleaner(seq): 
    # your code here
    one_arr = []
    greater_than_one_arr = []
    
    for x in range(len(seq)):
        if seq[x] <= 1:
            one_arr.append(seq[x])
        else:
            greater_than_one_arr.append(x)
    return (one_arr, greater_than_one_arr)
