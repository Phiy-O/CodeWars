# [ 7 kyu ] Reverse Words
def reverse_words(text):
    #go for it
    arr = []
    for x in range(len(text.split(' '))):
        arr.append(text.split(' ')[x][::-1])
    return ' '.join(arr)
