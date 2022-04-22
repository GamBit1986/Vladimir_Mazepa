tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '11А' ]
i = 0

def check_gen(tutors: list, klasses: list):
    # Проверку можно усложнить, чтобы проверялось сколько именно элементов с None добавить, но в условии этого не было
    if len(tutors) < len(klasses):
        tutors.append(None)
    elif len(tutors) == len(klasses):
        pass
    else:
        klasses.append(None)
    gen_tutors = ((tutors[i], klasses[i]) for i in range(len(tutors)))
    yield gen_tutors




generator = check_gen(tutors, klasses)

# добавьте здесь доказательство, что создали именно генератор

print(*next(generator), sep='\n')
print(type(generator))

# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration