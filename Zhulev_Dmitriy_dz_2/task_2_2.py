def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    new_list = []
    for elem in list_in:
        if not elem.isdigit() and not elem.startswith('+') and not elem.startswith('-'):
            new_list.append(elem)
        if elem.isdigit() and len(elem) == 1:
            new_elem = f'"0{elem}"'
            new_list.append(new_elem)
        if elem.isdigit() and len(elem) == 2:
            new_list.append(f'"{elem}"')
        if (elem.startswith('+') or elem.startswith('-')) and len(elem) == 3:
            new_list.append(f'"{elem}"')
        if (elem.startswith('+') or elem.startswith('-')) and len(elem) == 2:
            elem = elem[0] + '0' + elem[1]
            new_list.append(f'"{elem}"')
            
    str_out = " ".join(new_list)
    
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
