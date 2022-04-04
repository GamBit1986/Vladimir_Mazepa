# Решение части b
i = 1
j = 0
list_of_cubes = []
summa = 0
number = 0
idx = 0
res2 = 0
def sum_digit(value):
    result = 0

    while value > 0:
        result += value % 10
        value //= 10
    return result

while i < 1000:
    list_of_cubes.append(i ** 3)
    i += 2
print(list_of_cubes)

while j < len(list_of_cubes):
    list_of_cubes[j] = list_of_cubes[j] + 17
    j += 1
print(list_of_cubes)

while idx < len(list_of_cubes):
    list_of_cubes[idx] = sum_digit(list_of_cubes[idx])
    idx += 1
print(list_of_cubes)

for element in list_of_cubes:
    if element % 7 == 0:
        res2 = res2 + element
print(res2)

