# [ 7 kyu ] String Matchup
def solve(a,b):
    result = []
    for x in b:
        result.append(a.count(x))
    return result
