
def convert_list_in_str(list_in: list) -> str:
    i = 0
    while i < len(list_in):
        sign = get_sign(list_in[i])
        print(sign)
        if list_in[i].isdigit() or (sign and list_in[i][1:].isdigit()):
            if sign:
                list_in[i] = sign + list_in[i][1:].zfill(2)
            else:
                list_in[i] = list_in[i].zfill(2)

            list_in.insert(i, '"')
            list_in.insert(i + 2, '"')
            i += 2
            print(i)

        i += 1
        print(i)

    str_out = ' '.join(list_in)
    return str_out

def get_sign(x):
    if x[0] in '+-':
        return x[0]


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

result = convert_list_in_str(my_list)
print(result)

