# Да се напише програма, която чете час от денонощието(цяло число)
# и ден от седмицата(текст) - въведени от потребителя и проверява дали офисът
# на фирма е отворен, като работното време на офисът е от 10-18 часа, от понеделник до събота включително

hour = int(input())
day = str(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == 'Saturday':
    if hour >= 10 and hour <= 18:
        print("open")
    else:
        print("closed")
elif day == "Sunday":
    print("closed")