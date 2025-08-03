# [ 7 kyu ] Count Cubes in a Menger Sponge
def calc_ms(n):
    # Happy coding!
    cube = 20
    if n == 0:
        return 1
    for x in range(1, n):
        cube *= 20
    return cube
