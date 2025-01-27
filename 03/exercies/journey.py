# Млад програмист разполага с определен бюджет и свободно време в даден сезон.
# Напишете програма, която да приема на входа бюджета и сезона,
# а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи.
# Ако е лято ще почива на къмпинг, а зимата в хотел.
# Ако е в Европа, независимо от сезона, ще почива в хотел.
# Всеки къмпинг или хотел, според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:
# · При 100 лв. или по-малко - някъде в България:
# o Лято - 30% от бюджета;
# o Зима - 70% от бюджета.
# · При 1000 лв. или по малко - някъде на Балканите:
# o Лято - 40% от бюджета;
# o Зима - 80% от бюджета.
# · При повече от 1000 лв. - някъде из Европа:
# o При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.

budget = float(input())
season = str(input())
destination = str()
place = str()
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        price = budget * 0.3
    elif season == 'winter':
        place = 'Hotel'
        price = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        price = budget * 0.4
    elif season == 'winter':
        place = 'Hotel'
        price = budget * 0.8
else:
    destination = 'Europe'
    place = 'Hotel'
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")