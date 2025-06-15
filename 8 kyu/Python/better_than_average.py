def better_than_average(class_points, your_points):
    # Your code here
    avg = sum(class_points) / len(class_points)
    if your_points > avg:
        return True
    return False
        
