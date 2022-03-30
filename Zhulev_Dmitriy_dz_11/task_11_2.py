from my_exception import CheckValue
    

try:
    num = int(input('Введите делимое: '))
    num_2 = int(input('Введите делитель: '))
    if num_2 == 0:
        raise CheckValue('На ноль делить нельзя!')
    print(round(num / num_2, 2))
except CheckValue as err:
    print(err)
