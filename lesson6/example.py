# import os
#
# folder = r'C:\Users\79262\PycharmProjects\homework_python\lesson6'
# # py_files = [os.path.join(folder,item)
# #             for item in os.listdir(folder)
# #             if item.lower().endswith('.py')]
# py_files = [item
#             for item in os.listdir(folder)
#             if item.lower().endswith('.py') or os.path.isdir(os.path.join(folder, item))]
# print(py_files)

# import os
from time import perf_counter
import random
#
# folder = r'C:\Users\79262\PycharmProjects\homework_python'
# letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
# for _ in range(100):
#     f_name = ''.join(random.sample(letters, random.randint(5, 10)))
#     f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
#     with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
#         f.write(f_content)


# bin_files = [item for item in os.listdir(folder)
#             if item.lower().endswith('.bin')]
#
# print(bin_files)
# start = perf_counter()
# size_threshold = 15 * 2 ** 10
# small_files = [item
#               for item in os.listdir(folder)
#               if os.stat(os.path.join(folder, item)).st_size < size_threshold]
# print(len(small_files), perf_counter() - start)
# # 155 2.271335837
# start = perf_counter()
# small_files_2 = [item.name
#                  for item in os.scandir(folder)
#                  if item.stat().st_size < size_threshold]
# print(len(small_files_2), perf_counter() - start)
# print(small_files == small_files_2)







import os
line = "".split('9')
print(line)
if line:
    print('Trueeeee!!!')
if '':
    print('222')








folder = r'C:\Users\79262\PycharmProjects\homework_python'
bin_files = [os.path.join(folder, item) for item in os.listdir(folder) if item.lower().endswith('.bin')]
# # print(os.path.join(folder, bin_files[0]))
# print(bin_files)
for f in bin_files:
    os.remove(f)
# folder = r'C:\Users\79262\PycharmProjects\homework_python'
# dir_name = os.path.join(folder, 'old_dir')
# print(dir_name)
# new_dir_name = os.path.join(folder,'../first_new_dir')
# print(os.path.join(folder, dir_name))
# if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#     print('11')
#     os.rename(dir_name, new_dir_name)
