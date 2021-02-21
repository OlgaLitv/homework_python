"""ЗАДАНИЕ 1

Человеко-ориентированное представление интервала времени
Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:

1) до минуты: <s> сек;
2) до часа: <m> мин <s> сек;
3) до суток: <h> час <m> мин <s> сек;
4) сутки или больше: <d> дн <h> час <m> мин <s> сек

Например, если пользователь введет 4567 секунд, вывести:
1 час 16 мин 7 сек"""
duration = int(input('введите число в секундах:'))
one_day = 86400
one_hour = 3600
one_minute = 60
if duration < one_minute:
    print(duration, 'сек')
elif duration > one_day:
    print(duration//one_day, 'дн', duration % one_day // one_hour, 'час', duration % one_day % one_hour // one_minute, 'мин', duration % one_minute, 'сек')
elif duration > one_hour:
    print(duration//one_hour, 'час', duration % one_hour//one_minute, 'мин', duration % one_minute, 'сек')
elif duration > one_minute:
    print(duration//one_minute, 'мин', duration % one_minute, 'сек')
