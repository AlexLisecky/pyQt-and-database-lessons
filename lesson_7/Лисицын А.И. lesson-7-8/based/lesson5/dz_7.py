import json

profit = {}
not_profit = {}
_sum = 0
_sum_sr = 0
i = 0


with open(r'/primer/text_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, form, money, not_money = line.split()
        profit[name] = int(money) - int(not_money)
        if profit.setdefault(name) > 0:
            _sum += profit.setdefault(name)
            i += 1
        else:
            not_profit[name] = profit[name]
    _sum_sr = _sum / i

print(f'Прибиль каждой компании: {profit},компании которые работают в убыток {not_profit}')
print(f'Средняя прибыль всех компаний: {_sum_sr}')


with open('file_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'json file:{js_str}')
