# [ 7 kyu ] Basic Math (Add or Subtract)
def calculate(s):
    # your code here
    import re
    arr = re.findall(r"\d+|[a-zA-Z]+", s)
    
    res = []
    for x in arr:
        if x == 'minus':
            x = '-'
        elif x == 'plus':
            x = '+'
        res.append(x)
    return str(eval(' '.join(res)))
