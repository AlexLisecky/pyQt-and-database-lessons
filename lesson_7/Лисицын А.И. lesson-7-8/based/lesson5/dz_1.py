# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open("my_file.txt", "w", encoding="utf-8")


while True:
    answer = input("Напишите строчку которую хотите записать: \n")
    my_file.writelines(answer + '\n')
    if answer == "":
        break

my_file.close()

my_f = open("my_file.txt", "r", encoding="utf-8")
content = my_f.read()
print(content)
my_f.close()


with open("my_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end='')
