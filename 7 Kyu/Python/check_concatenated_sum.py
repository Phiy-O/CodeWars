# [ 7 kyu ] Concatenated Sum
def check_concatenated_sum(n, t):
    arr = []
    
    if t == 0:
        return False
    
    for x in list(str(n)):
        if x in '123456789':
            arr.append(int(x * t))
            
    if n < 0:
        return -sum(arr) == n
    return sum(arr) == n
