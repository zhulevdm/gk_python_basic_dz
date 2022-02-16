#Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего.


def get_numbers(source: list):
    result = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
