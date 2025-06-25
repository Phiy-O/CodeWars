def get_count(sentence):
    vow = ['a', 'i', 'u', 'e', 'o']
    count = 0
    for x in list(sentence):
        if x in vow:
            count += 1
    return count
