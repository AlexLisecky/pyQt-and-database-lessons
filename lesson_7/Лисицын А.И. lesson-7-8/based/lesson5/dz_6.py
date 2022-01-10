# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


my_dict = {}


with open(r'/primer/text_6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        line = line.split()
        num_list = []
        for word in line:
            num = ''
            for i in word:
                my_dict[line[0]] = sum(num_list)
                if i.isdigit():
                    num += i
                else:
                    if num != '':
                        num_list.append(int(num))
                        num = ''

print(my_dict)
