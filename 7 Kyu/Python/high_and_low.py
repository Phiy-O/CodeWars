# [7 kyu ] Highest and Lowest
def high_and_low(numbers):
    # ...
    arr = []
    res = []
    for x in numbers.split(' '):
        arr.append(int(x))
    
    check = arr[0]
    cek = arr[0]
    for num in arr:
        if check >= num:
            check = num
        if cek <= num:
            cek = num
    res.append(str(cek))
    res.append(str(check))
        
    return ' '.join(res)
