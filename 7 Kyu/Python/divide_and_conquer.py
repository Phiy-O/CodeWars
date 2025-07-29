# [ 7 kyu ] Divide and Conquer
def div_con(x):
    # your code here
    result = 0
    str_arr = []
    
    for num in x:
        if isinstance(num, str):
            str_arr.append(int(num))
        else:
            result += num
    return result - sum(str_arr)
