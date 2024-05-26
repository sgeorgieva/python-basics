# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
# че решават да отидат на риболов с кораб. Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# · Цената за наем на кораба през пролетта е 3000 лв.;
# · Цената за наем на кораба през лятото и есента е 4200 лв.;
# · Цената за наем на кораба през зимата е 2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# · Ако групата е до 6 човека включително - отстъпка от 10%;
# · Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
# · Ако групата е от 12 нагоре - отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой,
# освен ако не е есен - тогава нямат допълнителна отстъпка,
# която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.

# constants - seasons
SEASON_SPRING = 'Spring'
SEASON_SUMMER = 'Summer'
SEASON_AUTUMN = 'Autumn'
SEASON_WINTER = 'Winter'
# constants - prices
PRICE_RENT_SHIP_SPRING = 3000
PRICE_RENT_SHIP_SUMMER = 4200
PRICE_RENT_SHIP_AUTUMN= 4200
PRICE_RENT_SHIP_WINTER = 2600
# constants - discounts
FISHERS_COUNT_LOW = 6
FISHERS_COUNT_MID_LOW_RANGE = 7
FISHERS_COUNT_MID_HIGH_RANGE = 11
FISHERS_COUNT_HIGH = 12
LOW_DISCOUNT = 0.1
MIDDLE_DISCOUNT = 0.15
HIGH_DISCOUNT = 0.25
DISCOUNT_EVENT = 0.05

budget = int(input())
season = input().strip()
fishers = int(input())

price = 0

if season == SEASON_SPRING:
    price = PRICE_RENT_SHIP_SPRING
elif season == SEASON_SUMMER:
    price = PRICE_RENT_SHIP_SUMMER
elif season == SEASON_AUTUMN:
    price = PRICE_RENT_SHIP_AUTUMN
elif season == SEASON_WINTER:
    price = PRICE_RENT_SHIP_WINTER
else:
    print("Invalid season")
    exit()

if fishers <= FISHERS_COUNT_LOW:
    price -= price * LOW_DISCOUNT
elif FISHERS_COUNT_MID_LOW_RANGE <= fishers <= FISHERS_COUNT_MID_HIGH_RANGE:
    price -= price * MIDDLE_DISCOUNT
else:
    price -= price * HIGH_DISCOUNT

if season != SEASON_AUTUMN and fishers % 2 == 0:
    price -= price * DISCOUNT_EVENT

if budget >= price:
    remaining_money = budget - price
    print(f"Yes! You have {remaining_money:.2f} leva left.")
else:
    needed_money = price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")