def is_opposite(s1,s2):
    # your code here
    if not (s1 or s2):
        return False
    
    for x in range(len(s1)):
        if s1[x] == s2[x]:
            return False
    
    return True
