# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23,
# а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо

hours = int(input())
minutes = int(input())

# minutes + 15 > 59 and
# hours <= 23
if (minutes + 15) - 60 <= 9:
    print('here')
    print(f'{hours if hours <= 23 or hours == 0 else 0}:{f"0{(minutes + 15) - 60 if ((minutes + 15) - 60) <= 9 else (minutes + 15) - 60}"}')
else:
    print('here2')
    print(f"{hours + 1 if hours + 1 <= 23 or hours == 0 else 0}:{minutes+15 if ((minutes + 15) - 60) <= 9 else (minutes + 15) - 60}")