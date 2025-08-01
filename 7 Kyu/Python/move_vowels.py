# [ 7 kyu ] Move All Vowels
def move_vowels(input): 
    result = ''
    word = ''
    for x in input:
        if x.lower() in 'aiueo':
            result += x
            continue
        else:
            word += x
    return word + result
