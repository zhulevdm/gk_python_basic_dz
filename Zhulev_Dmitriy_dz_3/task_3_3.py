def thesaurus(*args) -> dict:
    dict_out = {}
    
    for letter in map(chr, range(1040, 1072)):
        list_val = list(filter(lambda x: x.startswith(letter), args))
        if list_val:
            dict_out[letter] = list_val
     
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
    