def is_it_a_num(s: str) -> str:
    n = ''
    for x in list(s):
        if x.isdigit():
            n += x
    if len(n) == 11 and "0" in n:
        return n
    return "Not a phone number"
