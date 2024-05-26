# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята,
# че Ви убеждава да напишете програма, която да изчисли колко ще им струва,
# за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.
# Различните цветя са с различни цени:

ROSE_PRICE = 5
DAHLIA_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_RICE = 3
GLADIOLUS_RICE = 2.50
total_price = 0

type_flower = str(input())
count_flowers = int(input())
budget = int(input())

if type_flower == "Roses":
    total_price = count_flowers * ROSE_PRICE
    if count_flowers > 80:
        total_price = total_price * 0.90
elif type_flower == "Dahlias":
    total_price = count_flowers * DAHLIA_PRICE
    if count_flowers > 90:
        total_price = total_price * 0.85
elif type_flower == 'Tulips':
    total_price = count_flowers * TULIPS_PRICE
    if count_flowers > 80:
        total_price = total_price * 0.85
elif type_flower == 'Narcissus':
    total_price = count_flowers * NARCISSUS_RICE
    if count_flowers < 120:
        total_price = total_price * 1.15
elif type_flower == 'Gladiolus':
    total_price = count_flowers * GLADIOLUS_RICE
    if count_flowers < 80:
        total_price = total_price * 1.20

if total_price > budget:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {budget - total_price:.2f} leva left.")