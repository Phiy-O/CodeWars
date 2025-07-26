# [ 7 kyu ] Spot the Differences
def spot_diff(s1, s2):
    arr = []
    for x in range(len(s1)):
        if s2[x] != s1[x]:
            arr.append(x)
    return arr
