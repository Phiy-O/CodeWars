# [ 7 kyu ] The Hidden Word
def hidden(num):
    # Code here
    result = ''
    dict_keys = {6: "a", 1: "b" , 7: "d", 4: "e", 3: "i", 2: "l", 9: "m", 8: "n", 0: "o", 5: "t"}
    for x in list(str(num)):
        result += dict_keys[int(x)]
    return result
