def travel_distance(avg_speed, travel_time):
    knot = 1.852 # km/jam
    travel_hours = travel_time / 60
    return avg_speed * knot * travel_hours
