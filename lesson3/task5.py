""" Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]


Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда
каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""


from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num, repeat=True):
    """function returns num choices, with repeat or without repeat"""
    output_lst = []
    if num > 5:
        num = 5
    for i in range(num):
        word1, word2, word3 = choice(nouns), choice(adverbs), choice(adjectives)
        if not repeat:
            nouns.remove(word1)
            adverbs.remove(word2)
            adjectives.remove(word3)
        output_lst.append(word1 + " " + word2 + " " + word3)
    return output_lst


n = int(input('Какое количество шуток поднимет вам настроение?'))
print(get_jokes(n, repeat=False))
