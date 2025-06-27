def even_and_odd(n): 
    # your code here
    odd_arr = []
    even_arr = []
    n = list(str(n))
    for x in n:
        if int(x) % 2 == 0:
            odd_arr.append(x)
        else:
            even_arr.append(x)
    odd_num = ''.join(odd_arr)
    even_num = ''.join(even_arr)
    if len(even_arr) == 0:
        even_num = '0'
    elif len(odd_num) == 0:
        odd_num = '0'
    return (int(odd_num), int(even_num))
