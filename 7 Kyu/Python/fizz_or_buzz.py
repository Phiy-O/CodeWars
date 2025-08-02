# [ 7 kyu ] Fizz/Buzz
def solution(number):
    a = 0
    b = 0
    c = 0
    for x in range(1, number):
        if x % 3 == 0 and x % 5 == 0:
            c += 1
        elif x % 3 == 0:
            a += 1
        elif x % 5 == 0:
            b += 1
    return [a, b, c]
