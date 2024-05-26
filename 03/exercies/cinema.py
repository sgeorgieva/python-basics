# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
# Има три вида прожекции с билети на различни цени:
# · Premiere - премиерна прожекция, на цена 12.00 лева;
# · Normal - стандартна прожекция, на цена 7.50 лева;
# · Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа),
# въведени от потребителя, и изчислява общите приходи от билети при пълна зала.
# Резултатът да се отпечата във формат 2 знака след десетичната точка.

TICKET_PREMIERE = 12
TICKET_NORMAL = 7.50
TICKET_DISCOUNT = 5
income = 0

type_projection = str(input())
count_rows_of_hall = int(input())
count_columns_of_hall = int(input())

if type_projection == 'Premiere':
    income = count_rows_of_hall * count_columns_of_hall * TICKET_PREMIERE
elif type_projection == 'Normal':
    income = count_rows_of_hall * count_columns_of_hall * TICKET_NORMAL
elif type_projection == 'Discount':
    income = count_rows_of_hall * count_columns_of_hall * TICKET_DISCOUNT
print(f"{income:.2f} leva")