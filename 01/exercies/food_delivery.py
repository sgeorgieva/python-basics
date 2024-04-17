# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# • Пилешко меню – 10.35 лв.
# • Меню с риба – 12.40 лв.
# • Вегетарианско меню – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.

CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DESERT_MENU_PRICE = 20/100
DELIVERY_PRICE = 2.50

chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

menu_total_price = (chicken_menus * CHICKEN_MENU_PRICE) + (fish_menus * FISH_MENU_PRICE) + (vegetarian_menus * VEGETARIAN_MENU_PRICE)
total_desert_price = menu_total_price * DESERT_MENU_PRICE

total_price = menu_total_price + total_desert_price + DELIVERY_PRICE

print(f'{total_price:.2f}')