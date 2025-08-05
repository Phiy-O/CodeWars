# [ 7 kyu ] Valid Parentheses
def valid_parentheses(paren_str):
    result = []
    for x in paren_str:
        if x == "(":
            result.append(x)
        elif x == ")":
            if len(result) == 0:
                return False
            result.pop()
            
    return len(result) == 0
    
    
