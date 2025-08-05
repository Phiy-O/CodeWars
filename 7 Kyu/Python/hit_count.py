# [ 7 kyu ] Hit Count
def counter_effect(hit_count):
    # your code here
    arr = []
    for x in hit_count:
        result = [y for y in range(0, int(x) + 1)]
        arr.append(result)
    return arr
