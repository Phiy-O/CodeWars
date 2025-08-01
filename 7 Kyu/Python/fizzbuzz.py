# [ 7 kyu ] Fizz Buzz
def fizzbuzz(n):
    result = []
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            result.append('FizzBuzz')
        elif x % 5 == 0:
            result.append('Buzz')
        elif x % 3 == 0:
            result.append('Fizz')
        else:
            result.append(x)
    return result    
