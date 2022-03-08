import functools


def type_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        list_args = []
        for i in args:
            list_args.append(f'{func.__name__}({i}:{type(i)})')
        print(f'{",".join(list_args)}')
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3
