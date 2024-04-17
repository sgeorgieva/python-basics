# Джеси решава, че иска да се занимава с баскетбол, но за да тренира е нужна екипировка.
# Напишете програма, която изчислява какви разходи ще има Джеси, ако започне да тренира,
# като знаете колко е таксата за тренировки по баскетбол за период от 1 година. Нужна екипировка:
# • Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# • Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# • Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# • Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

year_tax_exercises = int(input())
BASKETBALL_SHOES = year_tax_exercises - (year_tax_exercises * (40/100))
BASKETBALL_OUTFIT = BASKETBALL_SHOES - (BASKETBALL_SHOES * (20/100))
BASKETBALL_BALL = BASKETBALL_OUTFIT / 4
BASKETBALL_ACCESSORIES = BASKETBALL_BALL / 5

total_price_expenses = year_tax_exercises + BASKETBALL_SHOES + BASKETBALL_OUTFIT + BASKETBALL_BALL + BASKETBALL_ACCESSORIES

print(total_price_expenses)