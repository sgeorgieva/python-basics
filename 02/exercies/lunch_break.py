# По време на обедната почивка искате да изгледате епизод от своя любим сериал.
# Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно време
# да изгледате епизода. По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка
import math

name_serial = str(input())
duration_time_per_episode = int(input())
duration_time_per_break = int(input())

lunch_time = duration_time_per_break * 8
break_time = duration_time_per_break / 4


total_time = duration_time_per_break - (lunch_time + break_time)

if total_time >= duration_time_per_episode:
    print(f"You have enough time to watch {name_serial} "
          f"and left with "f"{math.ceil(total_time - duration_time_per_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need "
          f"{math.ceil(duration_time_per_episode - total_time)} more minutes.")