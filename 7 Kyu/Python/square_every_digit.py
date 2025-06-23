def square_digits(num):
    # Your code here
    n = list(str(num))
    res = ''
    for x in n:
        x = int(x) ** 2
        res += str(x)
    return int(res)
