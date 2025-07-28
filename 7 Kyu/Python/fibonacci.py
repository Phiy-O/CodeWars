# [ 7 kyu ] Fibonacci
def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    arr = [0 , 1]
    for x in range(1, n):
        arr.append(arr[-1] + arr[-2])
    if n == 0:
        return 0
    return arr[len(arr) - 1]
