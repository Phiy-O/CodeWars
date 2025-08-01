# [ 7 kyu ] Sum - Square Even, Root Odd
def sum_square_even_root_odd(nums):
    square_even = []
    root_odd = []
    for x in nums:
        if x % 2 == 0:
            square_even.append(x**2)
        else:
            root_odd.append(x**(1/2))
    return round(sum(square_even) + sum(root_odd), 2)
