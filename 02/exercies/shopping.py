# Петър иска да купи N видеокарти, M процесора и P на брой рам памет.
# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка.
# Важат следните цени:
# · Видеокарта – 250 лв./бр.
# · Процесор – 35% от цената на закупените видеокарти/бр.
# · Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

VIDEO_CARD_PRICE = 250

budget = float(input())
count_video_cards = int(input())
count_processors = int(input())
count_ram_memory = int(input())

video_card_price = count_video_cards * VIDEO_CARD_PRICE
processors_price = count_processors * (0.35 * video_card_price)
ram_memory_price = count_ram_memory * (0.10 * video_card_price)

total_price = video_card_price + processors_price + ram_memory_price

if count_video_cards > count_processors:
    total_price = total_price - (total_price * 0.15)

if total_price > budget:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
else:
    print(f"You have {budget - total_price:.2f} leva left!")
