# Учебната година вече е започнала и отговорничката на 10Б клас -
# Ани трябва да купи определен брой пакетчета с химикали, пакетчета с маркери,
# както и препарат за почистване на дъска. Тя е редовна клиентка на една книжарница,
# затова има намаление за нея, което представлява някакъв процент от общата сума.
# Напишете програма, която изчислява колко пари ще трябва да събере Ани,
# за да плати сметката, като имате предвид следния ценоразпис:
#
# • Пакет химикали - 5.80 лв.
# • Пакет маркери - 7.20 лв.
# • Препарат - 1.20 лв (за литър)

# Вход
# От конзолата се четат 4 числа:
# · Брой пакети химикали - цяло число в интервала [0...100]
# · Брой пакети маркери - цяло число в интервала [0...100]
# · Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# · Процент намаление - цяло число в интервала [0...100]

PENS_PRICE_PER_PACKAGE = 5.80
MARKER_PRICE_PER_PACKAGE = 7.20
LITERS_OF_PREPARATION_PER_PACKAGE = 1.20

pens_count_per_package = int(input())
marker_count_per_package = int(input())
liters_of_preparation_count_per_package = int(input())
discount_percent = int(input()) / 100

total_price_pens_per_package = PENS_PRICE_PER_PACKAGE * pens_count_per_package
total_price_marker_per_package = MARKER_PRICE_PER_PACKAGE * marker_count_per_package
total_price_liters_of_preparation_per_package = LITERS_OF_PREPARATION_PER_PACKAGE * liters_of_preparation_count_per_package

total_price = total_price_pens_per_package + total_price_marker_per_package + total_price_liters_of_preparation_per_package
total_discount = total_price - (total_price * discount_percent)

print(f'Total price: {total_price_pens_per_package}')
