# [ 7 kyu ] Find the capitals
def capitals(word):
    #your code here
    arr = []
    for x in range(len(word)):
        if word[x].isupper():
            arr.append(x)
    return arr
