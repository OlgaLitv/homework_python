"""ЗАДАНИЕ 3

Сумма чисел из списка *
Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):

1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!

2) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
сумма цифр которых делится нацело на 7.

3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков"""
MAX_NUMBER = 1000
index = 1
cubes = []
while index < MAX_NUMBER:
    cubes.append(index ** 3)
    index +=2
summ = 0
for cube in cubes:
    sum_of_digites = 0
    current_number = cube
    while current_number > 0:
        sum_of_digites += current_number % 10
        current_number = current_number // 10
    if sum_of_digites % 7 == 0:
        summ += cube
print('ответ к пункту 1:', summ)

# пункт 2
summ = 0
for cube in cubes:
    sum_of_digites = 0
    current_number = cube + 17
    while current_number > 0:
        sum_of_digites += current_number % 10
        current_number = current_number // 10
    if sum_of_digites % 7 == 0:
        summ += cube + 17
print('ответ к пункту 2:', summ)

# пункт 3
summ = 0
index = 1
while index < MAX_NUMBER:
    sum_of_digites = 0
    current_number = index ** 3 + 17
    current = current_number
    while current_number > 0:
        sum_of_digites += current_number % 10
        current_number = current_number // 10
    if sum_of_digites % 7 == 0:
        summ += current
    index += 2
print('ответ к пункту 3:', summ)
