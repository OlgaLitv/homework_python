"""Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую
словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с
соответствующей буквы. Например:
>>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""


def thesaurus(*args):
    sorted_names = sorted(args)
    output_dict = {}
    for name in sorted_names:
        #print('___', name)
        if name[0] not in output_dict:
            print('___', name)
            same_letters_names = filter(lambda el: el.startswith(name[0]), args)
            output_dict[name[0]] = [*same_letters_names]
    return output_dict


print(thesaurus('Мария', 'Иван', 'Игорь', 'Матвей', 'Инна', 'Жанна', 'Зоя'))
