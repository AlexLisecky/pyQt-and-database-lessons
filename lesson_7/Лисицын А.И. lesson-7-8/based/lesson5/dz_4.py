# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_word = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
new_list = []


with open(r'/primer/text_4.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        line = line.split()
        new_list.append(rus_word[line[0]] + ' - ' + line[2])


with open('my_file_2.txt', 'w', encoding='utf-8') as my_file_2:
    for line in new_list:
        my_file_2.writelines(line + '\n')
