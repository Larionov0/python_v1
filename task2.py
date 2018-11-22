from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import *


from task1 import addUserDish


#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserDishValidator():
    #TODO
    passport = getUserPassport()
    while not passport:
        print("Incorrect passport")
        passport = getUserPassport()


    country = getCountryName()
    while not country:
        print("Incorrect country")
        country = getUserPassport()

    dish = getDishName()
    while not dish:
        print("Incorrect dish")
        dish = getUserPassport()

    addUserDish(passport, country, dish)



print("Task 1")
addUserDishValidator()
print(dataset)


print("\n\n")