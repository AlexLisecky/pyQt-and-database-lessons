# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input('Введите номер месяца от 1 до 12: '))
number_lst = []
season_lst = ['Зима', 'Весна', 'Лето', 'Осень']

while True:
    if 0 < number < 13:
        number_lst.append(number)
        break
    else:
        number = int(input('Введите номер месяца от 1 до 12: '))

if 12 or 1 or 2 in number_lst:
    print(f'Введенный месяц относится к {season_lst[0]}')
elif 3 or 4 or 5 in number_lst:
    print(f'Введенный месяц относится к {season_lst[1]}')
elif 6 or 7 or 8 in number_lst:
    print(f'Введенный месяц относится к {season_lst[2]}')
else:
    print(f'Введенный месяц относится к {season_lst[3]}')

