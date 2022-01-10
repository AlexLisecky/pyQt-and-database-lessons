from sys import argv

file_name, work_hour, pay, prize = argv

result = int(work_hour) * int(pay) + int(prize)
print(f'Заработная плата сотрудника: {result}')

# Заработная плата сотрудника: 20300
