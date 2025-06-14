def calculate_tip(amount, rating):
    #your code here
    import math
    
    result = 0
    
    if rating.lower() == 'terrible':
        result = amount * 0
    elif rating.lower() == 'poor':
        result = amount * 0.05
    elif rating.lower() == 'excellent':
        result = amount * 0.2
    elif rating.lower() == 'great':
        result = amount * 0.15
    elif rating.lower() == 'good':
        result = amount * 0.1
    else:
        return 'Rating not recognised'
    
    return math.ceil(result)
