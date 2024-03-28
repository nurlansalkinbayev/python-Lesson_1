# Сдаем бутылки
# Определим цену за бутылки
COST_1_LITP=0.1
COST_MORE_LITP=0.25
# Запрашиваем у пользователя колиество бутылок
bottle_1=int(input('Количество бутылок 1 литра? '))
bottle_more_1=int(input('Количество бутылок больше 1 литра?'))
# Рассчет суммы за бутылки
bill=bottle_1*COST_1_LITP+bottle_more_1*COST_MORE_LITP
print(f"Вашa сумма за бутылки: ${bill}")