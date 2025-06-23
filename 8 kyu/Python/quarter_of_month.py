def quarter_of(month):
    # your code here
    q = 0
    if 1 <= month <= 12:
        if 1 <= month <= 3:
            q = 1
        elif 4 <= month <= 6:
            q = 2
        elif 7 <= month <= 9:
            q = 3
        elif 10 <= month <= 12:
            q = 4
        else:
            q = 0
        return q
    return f"Test failed with month = {month}"
