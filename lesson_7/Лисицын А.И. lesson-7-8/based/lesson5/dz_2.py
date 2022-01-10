# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
lines = 0
word = 0


with open("my_file.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        lines += 1
        pos = 'out'
        for letter in line:
            if letter != ' ' and pos == 'out':
                word += 1
                pos = 'in'
            elif letter == ' ':
                pos = 'out'

print(f"Количество строк в файле: {lines}")
print(f'Количество слов в файле: {word}')

# строка 1 sdfsdf sdfs 2
# dfdsf wae awdas2
# sadfs 24
