# [ 7 kyu ] Multiply Word in String
def modify_multiply(st, loc, num):
    word = st.split()
    res = []
    for x in range(0, num):
        res.append(word[loc])
    return '-'.join(res)
