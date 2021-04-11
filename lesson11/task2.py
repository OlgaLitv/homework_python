"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на
данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой."""


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


num1, num2 = map(int, input('Введите 2 числа').split())
try:
    if num2 == 0:
        raise MyException('Деление на 0 запрещено!')
    print(f'результат: {num1} / {num2} = ', num1 / num2)
except MyException as err:
    print(err)
