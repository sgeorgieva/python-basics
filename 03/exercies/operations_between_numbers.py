# Напишете програма, която чете две цели числа (N1 и N2)
# и оператор, с който да се извърши дадена математическа операция.
# Възможните операции са: Събиране(+), Изваждане(-), Умножение(*), Деление(/) и Модулно деление(%).
# При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен.
# При обикновеното деление - резултата.
# При модулното деление - остатъка.
# Трябва да се има предвид, че делителят може да е равен на 0 (нула), а на нула не се дели.
# В този случай трябва да се отпечата специално съобщениe

number_1 = int(input())
number_2 = int(input())
operator = str(input())
operation = str()
result = str()

if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = number_1 + number_2
        if result % 2 == 0:
            operation = "even"
        else:
            operation = "odd"
    elif operator == '-':
        result = number_1 - number_2
        if result % 2 == 0:
            operation = "even"
        else:
            operation = "odd"
    else:
        result = number_1 * number_2
        if result % 2 == 0:
            operation = "even"
        else:
            operation = "odd"
    print(f"{number_1} {operator} {number_2} = {result} - {operation}")
elif operator == '/' or operator == '%':
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    elif operator == '/':
        result = number_1 / number_2
        print(f"{number_1} {operator} {number_2} = {result:.2f}")
    else:
        result = number_1 % number_2
        print(f"{number_1} {operator} {number_2} = {result}")
