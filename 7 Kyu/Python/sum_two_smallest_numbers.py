# [ 7 kyu ] Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    result = []
    sortedArray = sorted(numbers)
    result.append(sortedArray[0:2])
    for x in result:
        return sum(x)
