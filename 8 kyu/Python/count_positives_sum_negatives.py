def count_positives_sum_negatives(arr):
    num = 0
    min_num = 0
    result = []
        
    for x in arr:
        if x > 0:
            num += 1
        if x < 0:
            min_num += x
        result = [num, min_num]
    return result
