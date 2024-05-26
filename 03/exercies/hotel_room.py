# Хотел предлага 2 вида стаи: студио и апартамент.
# Напишете програма, която изчислява цената за целия престой за студио и апартамент.
# Цените зависят от месеца на престоя:

# constants for months
MONTH_AUGUST = 'August'
MONTH_SEPTEMBER = 'September'
MONTH_OCTOBER = 'October'
# constants for prices
PRICE_STUDIO_MAY_OCTOBER = 50
PRICE_APARTMENT_MAY_OCTOBER = 65
PRICE_STUDIO_JUNE_SEPTEMBER = 75.20
PRICE_APARTMENT_JUNE_SEPTEMBER = 68.70
PRICE_STUDIO_JULY_AUGUST = 76
PRICE_APARTMENT_JULY_AUGUST = 77
# constants for discounts
DISCOUNT_APARTMENT_NIGHTS_COUNT = 14
DISCOUNT_APARTMENT_RATE = 10 / 100
DISCOUNT_STUDIO_NIGHTS_COUNT_MAY = 7
DISCOUNT_STUDIO_LOW_NIGHTS_COUNT_OCTOBER = 7
DISCOUNT_STUDIO_LOW_NIGHTS_RATE_MAY = 5 / 100
DISCOUNT_STUDIO_LOW_NIGHTS_RATE_OCTOBER = 5 / 100
DISCOUNT_STUDIO_HIGH_NIGHTS_RATE_OCTOBER = 3 / 100

price_studio = 0
price_apartment = 0

month = input()
count_overnight_stay = int(input())