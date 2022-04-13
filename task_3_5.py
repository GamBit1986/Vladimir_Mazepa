import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    i = 0
    while i < count:
        for noun, adv, adj in zip(nouns, adverbs, adjectives):
            """
            В этом цикле я перемешал списки по одному, но перемешивание происходит в каждой итерации.
            Добавил по элементу из списка, чтобы создать строку
            А после разделил по запятой и добавил в общий список методом .split
            """
            random.shuffle(nouns)
            random.shuffle(adjectives)
            random.shuffle(adverbs)
            joke = (f'{noun}, {adv}, {adj}').split(', ')
            list_out.append(joke)
            list_out = list_out[:count]
        i += 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))


# def get_jokes_adv(count: int, repeat=True) -> list:
#     """Возвращает список шуток в количестве count"""
#     list_out = []
#     i = 0
#     while i < count:
#         for noun, adv, adj in zip(nouns, adverbs, adjectives):
#             """
#             В этом цикле я перемешал списки по одному, но перемешивание происходит в каждой итерации.
#             Добавил по элементу из списка, чтобы создать строку
#             А после разделил по запятой и добавил в общий список методом .split
#             """
#             random.shuffle(nouns)
#             random.shuffle(adjectives)
#             random.shuffle(adverbs)
#             joke = (f'{noun}, {adv}, {adj}').split(', ')
#             list_out.append(joke)
#             list_out = list_out[:count]
#         i += 1
#     return list_out