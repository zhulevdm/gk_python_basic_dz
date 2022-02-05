from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и 
        формирует из них единую строковую переменную разделяя значения запятой."""
    str_out = ''
    for elem in my_list:
        data_in = str(elem).split('.')
        if len(data_in) == 1:
            data_out = f'{data_in[0]} руб 00 коп'
        elif len(data_in) == 2 and len(data_in[1]) == 1:
            data_out = f'{data_in[0]} руб 0{data_in[1]} коп'
        else:
            data_out = f'{data_in[0]} руб {data_in[1]} коп'
        str_out = str_out + ', ' + data_out
    str_out = str_out.lstrip(', ')
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


result_2 = sort_prices(my_list)
if id(my_list) == id(result_2):
    print('объект result_2 остался тем же объектом, что и my_list')
else:
    print('объект result_2 отличается от объекта my_list')
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_in.sort()
    list_out = list_in[-5:]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
