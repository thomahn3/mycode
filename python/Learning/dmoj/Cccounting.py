burger = input()
sides = input()
drink = input()
dessert = input()

if burger == "1":
    burger_calorie = 461
elif burger == "2":
    burger_calorie = 431
elif burger == "3":
    burger_calorie = 420
else:
    burger_calorie = 0

if drink == "1":
    drink_calorie = 130
elif drink == "2":
    drink_calorie = 160
elif drink == "3":
    drink_calorie = 118
else:
    drink_calorie = 0

if sides == "1":
    sides_calorie = 100
elif sides == "2":
    sides_calorie = 57
elif sides == "3":
    sides_calorie = 70
else:
    sides_calorie = 0

if dessert == "1":
    dessert_calorie = 167
elif dessert == "2":
    dessert_calorie = 266
elif dessert == "3":
    dessert_calorie = 75
else:
    dessert_calorie = 0

calorietotal = burger_calorie + drink_calorie + sides_calorie + dessert_calorie

print(f"Your total Calorie count is " + str(calorietotal) +".")