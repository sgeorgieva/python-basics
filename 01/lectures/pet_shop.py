# Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и котки.
# Храната се пазарува от зоомагазин, като една опаковка храна за кучета е на цена 2.50 лв,
# а опаковка храна за котки струва 4 лв

food_per_dogs = 2.5
food_per_cats = 4
dogs = int(input())
cats = int(input())
expenses_dogs = dogs * food_per_dogs
expenses_cats = cats * food_per_cats
expenses_all = expenses_dogs + expenses_cats

print(f"{expenses_all} lv.")
