lst = int(input('Введите длину списка: '))
my_list = []
i = 0

while i < lst:
    my_list.append(input('Введите значение в список: '))
    i += 1

print(f'Исходный список: {my_list}')

index = 0

for i in range(int(len(my_list) / 2)):
    my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
    index += 2

print(f'Переделанный список: {my_list}')
