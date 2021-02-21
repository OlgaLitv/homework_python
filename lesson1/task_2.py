"""ЗАДАНИЕ 2

Сумма цифр числа
Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".
"""
number = 1
while True:
    number = int(input('введите число:'))
    sum_of_digites = 0
    if number !=0:
        while number > 0:
            sum_of_digites += number % 10
            number = number // 10
        print('сумма цифр равна:', sum_of_digites)
    else:
        print('goodbay')
        break
