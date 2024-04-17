# Напишете програма, която изчислява колко часа ще са необходими на един архитект,
# за да изготви проектите на няколко строителни обекта.
# Изготвянето на един проект отнема три часа.

# 1. Името на архитекта - текст
# 2. Брой на проектите, които трябва да изготви - цяло число в интервала [0 … 100]

architect_name = input()
projects = int(input())

total_time = projects * 3

print(total_time)
print(f"The architect {architect_name} will need {total_time} hours to complete {projects} project/s.")