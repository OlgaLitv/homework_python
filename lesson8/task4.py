"""4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения
функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

#>>> a = calc_cube(5)
125
#>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?"""


import re

re_int = re.compile(r'[+-]?\d+')


def validate(valid_f):
    def val_checker(func):
        def tag_logger(*args, **kwargs):
            for arg in args:
                if not valid_f(arg):
                    raise ValueError('Input correct data, please')
            for _, kw in kwargs.items():
                if not valid_f(kw):
                    raise ValueError('Input correct data, please')
            try:
                answer = func(*args, **kwargs)
            except ZeroDivisionError:
                raise ValueError('Division by zero, input correct data, please')
            return answer
        return tag_logger
    return val_checker


@validate(lambda x: re_int.fullmatch(str(x)))
def calc_cube(x):
    return x ** 3


@validate(lambda x: re_int.fullmatch(str(x)))
def calc_degree(number=1, degree=1):
    return number ** degree


@validate(lambda x: re_int.fullmatch(str(x)))
def calc_division(num1, num2):
    return num1 / num2


@validate(lambda x: re_int.fullmatch(str(x)))
def calc_int_division(num1, num2):
    return num1 // num2


print('-7 в кубе равно', calc_cube(-7))
# print('1.5 в кубе равно', calc_cube(1.5))
print('-2 в степени 3 равно', calc_degree(degree=3, number=-2))
print('-2 в степени -3 равно', calc_degree(-2, -3))
print('32 делить на 2 равно', calc_division(32, 2))
print('32 mod 3 равно', calc_int_division(32, 3))
print('2 mod 0 равно', calc_int_division(2, 0))
