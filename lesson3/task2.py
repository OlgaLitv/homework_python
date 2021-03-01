"""*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""
# Решено с помощью функции из 1 задания


numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(number):
        return numbers.get(number, 'неправильный ввод')


def num_translate_adv(number):
    if number[0].isupper():
        return num_translate(number.lower()).capitalize()
    else:
        return num_translate(number.lower())


print(num_translate_adv(input('Input number, please:')))
