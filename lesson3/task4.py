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
    sort_lst = []
    #получаем список первых букв фамилий и сортируем его
    for name in args:
        surname_first_letter = name.split(' ')[::-1][0][:1]
        if not (surname_first_letter in sort_lst):
            sort_lst.append(surname_first_letter)
    sort_lst.sort()
    for letter in sort_lst:
        if not letter in output_dict:
            same_letters_names = filter(lambda el: el.split(' ')[1][0] == letter, args)
            output_dict[letter] = thesaurus(*same_letters_names)
    return output_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
