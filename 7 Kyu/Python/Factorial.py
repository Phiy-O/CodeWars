def factorial(n):
    if n == 0: 
        return 1
    else:
        if 12 >= n > 0:
            return n * factorial(n - 1)
        else:
            raise ValueError("error")
