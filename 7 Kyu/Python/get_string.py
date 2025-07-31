# [ 7 kyu ] Interview Question (easy)
def get_strings(city):
    object = {}
    result = []
    for x in city.lower().replace(' ', ''):
        object[x] = city.lower().count(x) * '*'
    
    for i in object.items():
        result.append(f'{i[0]}:{i[1]}')
    return ','.join(result)
