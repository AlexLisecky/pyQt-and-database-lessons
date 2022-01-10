"""
Модуль запрашивает время в секундах и выводит результат в H:M:S.
"""

user_time = int(input("Введите время в секундах: "))

HOURS = (user_time // 3600) % 24

MINUTES = (user_time // 60) % 60

SECOND = user_time % 60

if HOURS < 10:
    hours = "0" + str(HOURS)
if MINUTES < 10:
    minutes = "0" + str(MINUTES)
if SECOND < 10:
    second = "0" + str(SECOND)

print(f"Время на текущий момент {HOURS}:{MINUTES}:{SECOND}.")
