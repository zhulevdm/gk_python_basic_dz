def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    dictionary_num = {
        "one" : "один",
        "two" : "два",
        "three" : "три",
        "four" : "четыре",
        "five" : "пять",
        "six" : "шесть",
        "seven" : "семь",
        "eight" : "восемь",
        "nine" : "девять",
        "ten" : "десять"
        }
    if value.istitle() and value.lower() in dictionary_num:
        value = value.lower()
        str_out = dictionary_num.get(value).capitalize()
    else:
        str_out = dictionary_num.get(value)
    return str_out


print(num_translate_adv("one"))
print(num_translate_adv("Ten"))
print(num_translate_adv("Edfdfdf"))
    