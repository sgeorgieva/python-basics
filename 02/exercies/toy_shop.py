# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# · Пъзел - 2.60 лв.
# · Говореща кукла - 3 лв.
# · Плюшено мече - 4.10 лв.
# · Миньон - 8.20 лв.
# · Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

PUZZLE_PRICE = 2.6
TALKING_DOLL_PRICE = 3
PLUSH_BEAR_PRICE = 4.1
MINION_PRICE = 8.2
TRUCK_PRICE = 2

price_excursion = float(input())
puzzle_count = int(input())
talking_dolls_count = int(input())
plush_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = puzzle_count * PUZZLE_PRICE
talking_dolls_price = talking_dolls_count * TALKING_DOLL_PRICE
plush_bears_price = plush_bears_count * PLUSH_BEAR_PRICE
minions_price = minions_count * MINION_PRICE
trucks_price = trucks_count * TRUCK_PRICE

total_price = puzzle_price + talking_dolls_price + plush_bears_price + minions_price + trucks_price
toys_count = puzzle_count + talking_dolls_count + plush_bears_count + minions_count + trucks_count

if toys_count >= 50:
    total_price = total_price * 0.75

rent_price = total_price * (10 / 100)
price = total_price - rent_price


if price >= price_excursion:
    print(f"Yes! {price - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - price:.2f} lv needed.")