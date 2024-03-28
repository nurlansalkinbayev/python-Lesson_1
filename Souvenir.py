# интернет магазин сувениров 
# Определим количество сувениров и безделушек
number_souvenirs = int(input('Количество сувениров? '))
number_baubles = int(input('Количество безделушек? '))
# Определим вес сувениров и безделушек
weight_souvenir = 75
weight_bauble = 112
# Определим общий вес посылки
total_weight = (number_souvenirs * weight_souvenir + number_baubles * weight_bauble) / 1000
# Выводим результат
print(f'Общий вес посылки: {total_weight} кг.')
