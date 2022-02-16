def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    nums_gen = (num_out for num_out in range(1, number + 1, 2))
    return nums_gen


n = 21
generator = odd_nums(n)
for _ in range(1, n+1, 2):
    print(next(generator))

#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
