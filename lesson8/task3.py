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


def type_logger(func):

    def tag_logger(*args, **kwargs):
        answer = str(func.__name__) + '('
        for arg in args:
            answer += str(arg) + ': ' + str(type(arg)) + ', '
        for _, kw in kwargs.items():
            answer += str(kw) + ': ' + str(type(kw)) + ', '
        answer = answer[:-2] + ')'
        print('---type_logger:', answer)
        return func(*args, **kwargs)

    return tag_logger


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_degree(number=1, degree=1):
    return number ** degree


print('куб числа 3 равен', calc_cube(3))
print('4 в степени 2 равно ', calc_degree(degree=2, number=4))
print('5 в степени 3 равно ', calc_degree(5, degree=3))
