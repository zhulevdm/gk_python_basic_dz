# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке.


def get_uniq_numbers(src: list):
    uniq_numbers = set()
    temp = set()
    for num in src:
        if num not in temp:
            uniq_numbers.add(num)
        else:
             uniq_numbers.discard(num)
        temp.add(num)
    uniq_numbers_ord = [num for num in src if num in uniq_numbers]
    return uniq_numbers_ord


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))

#Ниже ещё одно решение без использования множеств, двумя списками. С сохранением порядка.

'''
def get_uniq_numbers(src: list):
    uniq_numbers = []
    temp = []
    for num in src:
        if num not in temp:
            uniq_numbers.append(num)
        else:
            if num in uniq_numbers:
                uniq_numbers.remove(num)
        temp.append(num)
    return uniq_numbers


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
'''
