# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число), въведени от потребителя,
# и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.

product = str(input())
city = str(input())
quantity = float(input())
price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = 0.50
        print(f'{quantity * price:.2f}')
    elif product == 'water':
        price = 0.80
        print(f'{quantity * price:.2f}')
    elif product == 'beer':
        price = 1.20
        print(f'{quantity * price:.2f}')
    elif product == 'sweets':
        price = 1.45
        print(f'{quantity * price:.2f}')
    elif product == 'peanuts':
        price = 1.60
        print(f'{quantity * price:.2f}')
elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.40
        print(f'{quantity * price:.2f}')
    elif product == 'water':
        price = 0.70
        print(f'{quantity * price:.2f}')
    elif product == 'beer':
        price = 1.15
        print(f'{quantity * price:.2f}')
    elif product == 'sweets':
        price = 1.30
        print(f'{quantity * price:.2f}')
    elif product == 'peanuts':
        price = 1.50
        print(f'{quantity * price:.2f}')
elif city == 'Varna':
    if product == 'coffee':
        price = 0.45
        print(f'{quantity * price:.2f}')
    elif product == 'water':
        price = 0.70
        print(f'{quantity * price:.2f}')
    elif product == 'beer':
        price = 1.10
        print(f'{quantity * price:.2f}')
    elif product == 'sweets':
        price = 1.35
        print(f'{quantity * price:.2f}')
    elif product == 'peanuts':
        price = 1.55
        print(f'{quantity * price:.2f}')