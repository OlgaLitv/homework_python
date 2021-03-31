"""Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего,
например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать оптимизацию кода
по памяти, по скорости.
"""

import time
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 56]

start = time.perf_counter()
result = (src[i] for i in range(1, len(src)) if src[i-1] < src[i])
# print([*result])
finish = time.perf_counter()
print([*result])
print('1 способ:', finish - start, sys.getsizeof(result))

start = time.perf_counter()
result = [src[i] for i in range(1, len(src)) if src[i-1] < src[i]]
# print(result)
finish = time.perf_counter()
print(result)
print('2 способ:', finish - start, sys.getsizeof(result))

# если печать результата идет до остановки счетчика, то 2 способ быстрее работает, если печать результата
# сделать после строки finish = time.perf_counter(), то быстрее 1 способ
