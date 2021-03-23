"""Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения из
влекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если
адрес не валиден, выбросить исключение ValueError. Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?"""
#
# import re
#
# RE_EMAIL = re.compile(r"\b['a'-'z']\w@\w")#\.['ru'|'com']
# def email_parse(str):
#     answer = RE_EMAIL.findall(str)
#     return answer
#
# print(email_parse('wqey@mail'))
# print(email_parse('awqe24y@mail.ru'))
# print(email_parse('3wqeey@mail'))
# print(email_parse('awqey@'))
# print(email_parse('wqey'))
# import yaml
#
# config = yaml.load('config.yaml')
# print(config)

import yaml

with open("config.yaml", 'r') as stream:
    try:
        load = yaml.safe_load(stream)
        print(type(load), load)
    except yaml.YAMLError as exc:
        print(exc)
