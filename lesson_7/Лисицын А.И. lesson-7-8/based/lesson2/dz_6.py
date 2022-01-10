good = []

while True:
    answer = input('Введите "Да" если хотите внести товар в список: ')
    if answer.lower() == 'да':
        number_goods = int(input('Введите номер товара: '))
        goods = {}
        while True:
            answer = input(
                'Введите "Да" если хотите внести в категорию товары параметры: ')
            if answer.lower() == 'да':
                goods_key = input("Введите параметр товара: ")
                goods_value = input("Введите пояснение для товара: ")
                goods[goods_key] = goods_value
            else:
                break
        good.append(tuple([number_goods, goods]))
    else:
        break
print(good)

result = {}

for i in good:
    for goods_key, goods_value in i[1].items():
        if goods_key in result:
            result[goods_key].append(goods_value)
        else:
            result[goods_key] = [goods_value]
print(result)
