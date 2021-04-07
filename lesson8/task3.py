"""3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

#>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести
тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать
работу декоратора? Сможете ли вывести имя функции, например, в виде:
#>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)"""

from functools import wraps


def type_logger(func):
    @wraps(func)
    def tag_logger(*args, **kwargs):
        answer = str(func.__name__) + '('
        for arg in args:
            answer += str(arg) + ': ' + str(type(arg)) + ', '
        for _, kw in kwargs.items():
            answer += str(kw) + ': ' + str(type(kw)) + ', '
        answer = answer[:-2] + ')'
        print('---type_logger:', answer)
        res = func(*args, **kwargs)
        # tag_logger.__doc__ = func.__doc__
        print('type of return value:', type(res))
        return res

    return tag_logger


@type_logger
def calc_cube(x):
    """calc_cube -  вычисляет куб числа"""
    return x ** 3


@type_logger
def calc_degree(number=1, degree=1):
    """ вычисляет число number  в степени degree """
    return number ** degree


print('куб числа 3 равен', calc_cube(3))
print('описание:', calc_cube.__doc__)
print('------------------------------------------------')
print('4 в степени 2 равно ', calc_degree(degree=2, number=4))
print('описание:', calc_degree.__doc__)
print('------------------------------------------------')
print('5 в степени 3 равно ', calc_degree(5, degree=3))
print('описание:', calc_degree.__doc__)
