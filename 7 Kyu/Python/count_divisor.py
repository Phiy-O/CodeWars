# [ 7 kyu ] Count the divisors of a number
def divisors(n):
    count = 0
    for x in range(1, n + 1):
        if n % x == 0:
            count += 1
    return count
