# [ 7 kyu ] Simple Fun #40: Timed Reading
def timed_reading(max_length, text):
    import re
    
    arr = []
    mod_text = re.sub(r"[@#$%^&*!?'']", "", text)
    for x in mod_text.split():
        if len(x) <= max_length:
            arr.append(x)
    return len(arr)
