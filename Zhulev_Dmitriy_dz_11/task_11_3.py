from my_exception import CheckValue
    

result = []
while True:
    try:
        num = input('Введите число, для остановки ввода введите слово stop: ')
        if num == 'stop':
            break
        if not num.isdigit():
            raise CheckValue('Вы ввели не число!')
        result.append(int(num))
    except CheckValue as err:
        print(err)

print(result)
