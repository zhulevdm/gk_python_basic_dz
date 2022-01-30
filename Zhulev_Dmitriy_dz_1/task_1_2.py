def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    result = 0
    for indx, num in enumerate(my_list):
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        if sum % 7 == 0:
            result += my_list[indx]

    return result  # Возвращаем значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    my_list = []
    for num in dataset:
        my_list.append(num + 17)

    result = 0
    for indx, num in enumerate(my_list):
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        if sum % 7 == 0:
            result += my_list[indx]

    return result  # Возвращаем значение полученной суммы


my_list = []  # Собераем нужный список по заданию
for i in range(1, 1000, 2):
    my_list.append(i ** 3)
print(my_list)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
