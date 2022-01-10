# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
new_list = []
pay = []
print('Список сотрудников: ')


with open(r'/primer/text_3.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        line = line.split()
        pay.append(float(line[1]))
        if float(line[1]) < 20000:
            new_list.append(line[0])
        print(line)

print('*' * 20)
print('Список сотрудников с зарплатой меньше 20к: ')


for x in new_list:
    print(x)

print(f'Средняя величина дохода сотрудников: {sum(pay) / len(pay)}')
