"""Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих
элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

import time
import sys


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = time.perf_counter()
unique_nums_set = set()
tmp1 = set()
for el in src:
    if el in tmp1:
        unique_nums_set.discard(el)
    else:
        unique_nums_set.add(el)
        tmp1.add(el)
unique_nums_ord = [el for el in src if el in unique_nums_set]
finish = time.perf_counter()
print('1 способ:', unique_nums_ord, finish - start, sys.getsizeof(unique_nums_ord))

start = time.perf_counter()
unique_nums = []
tmp2 = set()
for el in src:
    if el in tmp2:
        try:
            unique_nums.remove(el)
        except ValueError:
            pass
    else:
        unique_nums.append(el)
        tmp2.add(el)
finish = time.perf_counter()
print('2 способ:', unique_nums, finish - start, sys.getsizeof(unique_nums))


start = time.perf_counter()
unique = [x for x in src if src.count(x) == 1]
finish = time.perf_counter()
print('3 способ:', unique, finish - start, sys.getsizeof(unique))

start = time.perf_counter()
src1 = sorted(src)
l_src = len(src)
unique_brands = []
for i in range(l_src):
    if l_src == 1 or i == 0 and src1[i] != src1[i+1] \
            or 0 != i < l_src-1 and src1[i] != src1[i-1] and src1[i] != src1[i+1]\
            or 0 != i == l_src-1 and src1[i] != src1[i-1]:
        unique_brands.append(src1[i])
unique_brands_ord = [el for el in src if el in unique_brands]
finish = time.perf_counter()
print('4 способ:', unique_brands_ord, finish - start, sys.getsizeof(unique_brands_ord))

# на небольших списках 3 способ иногда бывает быстрее, но с ростом размера исходного списка быстрее становится 1 способ.
# 4 способ самый медленный и сложный
