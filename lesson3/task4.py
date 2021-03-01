""" *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей
буквы. Например:
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
"""


def thesaurus(*args):
    sorted_names = [*args]
    sorted_names.sort()
    output_dict = {}
    for name in sorted_names:
        if not name[0] in output_dict:
            same_letters_names = filter(lambda el: el.startswith(name[0]), args)
            output_dict[name[0]] = {*same_letters_names}
    return output_dict


def thesaurus_adv(*args):
    output_dict = {}
    for name in args:
        reverse_name = name.split(' ')[::-1]
        if not reverse_name[0][0] in output_dict:
            same_letters_names = filter(lambda el: el.split(' ')[1][0] == reverse_name[0][0], args)
            output_dict[reverse_name[0][0]] = thesaurus(*same_letters_names)
    return output_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
