def is_vow(inp):
    dict_vow = {"a":97, "i":105, "u":117, "e":101, "o":111}
    reverse_dict = {v: k for k, v in dict_vow.items()}
    for x in range(len(inp)):
        if inp[x] in dict_vow:
            inp[x] = dict_vow[inp[x]]
        elif inp[x] in reverse_dict:
            inp[x] = reverse_dict[inp[x]]
    return inp
