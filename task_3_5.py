import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# def get_jokes(count: int) -> list:
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
#
#
# print(get_jokes(2))
# print(get_jokes(10))


def get_jokes_adv(count: int, repeat=True) -> list:
    """
    Возвращает список шуток в количестве count если повтор разрешен, то схема, как в первой части, если нет,
    то просто мешаем кортежи, преобразуем в списки, собираем в список списков и выдаем срез по указанный счетчик
    Т.к. количество использований слов в шутке должно быть не больше одного, то шуток будет максимум 5
    """
    list_out = []
    i = 0

    if repeat == False:
        random.shuffle(nouns)
        random.shuffle(adjectives)
        random.shuffle(adverbs)
        list_nouns = list(nouns)
        list_adj = list(adjectives)
        list_adv = list(adverbs)
        joke_list = list(zip(list_nouns, list_adv, list_adj))

        for joke in joke_list:
            print(joke)
            list_out.append(list(joke))

        return list_out[:count]
    else:
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


print(get_jokes_adv(8, False))
print(get_jokes_adv(10))