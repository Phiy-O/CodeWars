def dating_range(age):
    if age <= 14:
        min = age - 0.1 * age
        max = age + 0.1 * age
    else:
        min = (age//2) + 7
        max = 2 * (age-7)
    return f"{int(min)}-{int(max)}"
