# Напишете програма, която изчислява каква сума ще получите в края на депозитния период
# при определен лихвен процент. Използвайте следната формула:

# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# От конзолата се четат 3 реда:
# 1. Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2. Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3. Годишен лихвен процент – реално число в интервала [0.00 …100.00]

deposit_price = float(input())
deposit_period = int(input())
year_interest_percent = float(input())

total_price = deposit_price + deposit_period * ((deposit_price * (year_interest_percent / 100)) / 12)

print(f'Total price: {total_price:.2f}')