# Иван решава да подобри Световния рекорд по плуване на дълги разстояния.
# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
# разстоянието в метри, което трябва да преплува и времето в секунди, за което плува разстояние от 1 м.
# Да се напише програма, която изчислява дали се е справил със задачата, като се има предвид, че:
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.
import math

DELAY_METERS = 15
DELAY_SECONDS = 12.5

record_seconds = float(input())
distance_per_meters = float(input())
time_per_seconds_about_distance_per_meters = float(input())

total_meters = distance_per_meters * time_per_seconds_about_distance_per_meters
time_delayed = math.floor((distance_per_meters / DELAY_METERS)) * DELAY_SECONDS

total_time = total_meters + time_delayed
if record_seconds <= total_time:
    print(f"No, he failed! He was {total_time - record_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

