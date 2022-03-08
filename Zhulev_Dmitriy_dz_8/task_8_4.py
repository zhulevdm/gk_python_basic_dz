import functools

def val_checker(func_check):
    def out(func):
        @functools.wraps(func)
        def wrapper(*args):
            func_check(*args)
            result = func(*args)
            return result
        return wrapper
    return out


def check_arg(a):
    if not type(a) == int or a < 0:
        msg = f'wrong val {a}'
        raise ValueError(msg)
    

@val_checker(check_arg)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
