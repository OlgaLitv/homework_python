"""1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера."""


data_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_logs:
    for line in file_logs:
        line1 = line.split('"')
        line2 = line1[1].split()
        data_list.append((line1[0].split()[0].strip(), line2[0], line2[1]))

with open('for_task1.txt', 'w', encoding='utf-8') as f:
    for user_item in data_list:
        f.write(user_item[0].strip() + ' ' + user_item[1] + ' ' + user_item[2] + '\n')
