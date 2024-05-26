# Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
# дали предвидените средства са достатъчни за снимането на филма.
# За снимките ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# · Декорът за филма е на стойност 10% от бюджета.
# · При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

budget = float(input())
statists = int(input())
clothes_per_statistic = float(input())

price_decor = budget * (10/100)
price_clothes = statists * clothes_per_statistic

if statists > 150:
    price_clothes -= price_clothes * 0.1


if price_decor + price_clothes <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - (price_decor + price_clothes):.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {price_decor + price_clothes - budget:.2f} leva more.")