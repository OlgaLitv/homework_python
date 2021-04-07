"""1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?
"""

import re
#----- вариант с компиляцией. Почему-то работает по-другому, проверяет начиная с 3 символа
re_email = re.compile(r'([a-z]\w*)@(\w+)\.ru|com')


def email_parse2(email):
    return re_email.fullmatch(email, re.IGNORECASE)
#-----


def email_parse(email):
    result = re.fullmatch(r'([a-z]\w*)@(\w+)\.ru|com', email, re.IGNORECASE)
    if result:
        return '{ username: ' + result.group(1) + ', domain: ' + result.group(2) + '}'
    else:
        raise ValueError('Input correct email, please')


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
print(email_parse('12someone@geekbrains.ru'))
print(email_parse('someone@.ru'))
print(email_parse('someone-geekbrains.ru'))
print(email_parse('someone-@geekbrains.ru'))
print('-------с компиляцией')
print(email_parse2('someone@geekbrains.ru'))
print(email_parse2('someone@geekbrainsru'))
print(email_parse2('12someone@geekbrains.ru'))
