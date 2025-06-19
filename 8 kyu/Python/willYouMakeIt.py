def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    car = (mpg * fuel_left) - distance_to_pump
    if car < 0:
        return False
    return True
