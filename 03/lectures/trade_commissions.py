# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число),
# въведени от потребителя, и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка. При невалиден град или обем на продажбите
# (отрицателно число) да се отпечата "error".

city = str(input())
volume_sells = float(input())

if city == 'Sofia':
    if 0 <= volume_sells <= 500:
        comission = volume_sells * 0.05
        print(f'{comission:.2f}')
    elif 500 < volume_sells <= 1000:
        comission = volume_sells * 0.07
        print(f'{comission:.2f}')
    elif 1000 < volume_sells <= 10000:
        comission = volume_sells * 0.08
        print(f'{comission:.2f}')
    elif volume_sells > 10000:
        comission = volume_sells * 0.12
        print(f'{comission:.2f}')
    else:
        print('error')
elif city == 'Varna':
    if 0 <= volume_sells <= 500:
        comission = volume_sells * 0.045
        print(f'{comission:.2f}')
    elif 500 < volume_sells <= 1000:
        comission = volume_sells * 0.075
        print(f'{comission:.2f}')
    elif 1000 < volume_sells <= 10000:
        comission = volume_sells * 0.1
        print(f'{comission:.2f}')
    elif volume_sells > 10000:
        comission = volume_sells * 0.13
        print(f'{comission:.2f}')
    else:
        print('error')
elif city == 'Plovdiv':
    if 0 <= volume_sells <= 500:
        comission = volume_sells * 0.055
        print(f'{comission:.2f}')
    elif 500 < volume_sells <= 1000:
        comission = volume_sells * 0.08
        print(f'{comission:.2f}')
    elif 1000 < volume_sells <= 10000:
        comission = volume_sells * 0.12
        print(f'{comission:.2f}')
    elif volume_sells > 10000:
        comission = volume_sells * 0.145
        print(f'{comission:.2f}')
    else:
        print('error')
elif city != 'Sofia' or city != 'Varna' or city != 'Plovdiv' or volume_sells < 0:
    print('error')