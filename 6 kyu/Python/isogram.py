def is_isogram(word):
    arr = []
    for letter in word.lower():
        if letter in arr:
            return False
        arr.append(letter)
    return True
