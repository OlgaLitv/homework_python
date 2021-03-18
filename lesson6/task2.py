"""2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из
предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера."""


data_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_logs:
    for line in file_logs:
        ip_address = line.split()[0]
        data_dict.setdefault(ip_address, 0)
        data_dict[ip_address] += 1
max_count = 0
for key, item in data_dict.items():
    if item > max_count:
        max_count = item
        ip_address = key
if max_count > 0:
    print(f"спамер {ip_address} отправил запросы {max_count} раз")
else:
    print('пустой файл')
