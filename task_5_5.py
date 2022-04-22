def get_uniq_numbers(src: list):
    unique_nums = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unique_nums.add(el)
        else:
            unique_nums.discard(el)
        tmp.add(el)

    unique_nums_ord = [el for el in src if el in unique_nums]

    return unique_nums_ord


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src), type(get_uniq_numbers(src)))