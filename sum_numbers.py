# Сумма первых n положительных чисел
# Запрашиваем число у пользователя
number = int(input('Введите положительное число:'))
# Вычисляем Сумму положительных чисел
sum = int((number * (number + 1)) / 2)
# Вывод Суммы положительных чисел
print(f'Сумма положительных чисел равна: {sum}')
