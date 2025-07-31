# [ 7 kyu ] Return a string's even characters.
def even_chars(st): 
    # your code here
    if len(st) < 2 or len(st) > 100:
        return 'invalid string'
    
    result = []
    for x in range(len(st)):
        if x % 2 != 0:
            result.append(st[x])
    return result
