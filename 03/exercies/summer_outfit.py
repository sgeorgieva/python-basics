# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ.
# Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече.
# Вашият приятел има различни планове за всеки етап от деня, които изискват
# и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# · Градусите - цяло число;
# · Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening.

degrees = int(input())
time_of_day = str(input())
outfit = str()
shoes = str()

if 10 <= degrees <= 18:
    if time_of_day == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif time_of_day == 'Afternoon' or time_of_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degrees <= 24:
    if time_of_day == 'Morning' or time_of_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif time_of_day == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif degrees >= 25:
    if time_of_day == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif time_of_day == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif time_of_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
