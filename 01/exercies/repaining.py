# Румен иска да пребоядиса хола и за целта е наел майстори.
# Напишете програма, която изчислява разходите за ремонта, предвид следните цени:
# · Предпазен найлон - 1.50 лв. за кв. метър
# · Боя - 14.50 лв. за литър
# · Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10%
# от количеството боя и 2 кв.м. найлон, разбира се и 0.40 лв. за торбички.
# Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30%
# от сбора на всички разходи за материали.

# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
# 1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2. Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3. Количество разредител (в литри) - цяло число в интервала [1…30]
# 4. Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
# Изход
# Да се отпечата на конзолата един ред:
# · "{сумата на всички разходи}"

NYLON_PRICE = 1.5
PAINT_PRICE = 14.5
ADDITIONAL_PAINT_RESOURCE_PRICE = 5

NYLON_BUFFER = 2.0
PAINT_BUFFER = 10/100
BAGS_EXPENSES = 0.4

LABOUR_MULTIPLIER = 30/100


nylon = int(input())
paint = int(input())
additional_paint_resource = int(input())
labour_hours = int(input())

nylon_total = (nylon + NYLON_BUFFER) * NYLON_PRICE
paint_total = (paint + (paint * PAINT_BUFFER)) * PAINT_PRICE
additional_paint_resource_total = additional_paint_resource * ADDITIONAL_PAINT_RESOURCE_PRICE

total_materials = nylon_total + paint_total + additional_paint_resource_total + BAGS_EXPENSES

price_per_hour = total_materials * LABOUR_MULTIPLIER
total_price_for_labour = labour_hours * price_per_hour

total_price = total_materials + total_price_for_labour

print(total_price)

