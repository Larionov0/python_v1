
"""
    Написати валідатор ....
    Правило валідації
"""

import re

def getUserPassport():

    user_input = input("Input the number of your passport: ")

    if (re.match(r"^[A-B]{2}\d{6}&", user_input) ):
        print(1)
        return user_input
    else:
        return False


"""
    Написати валідатор ....
    Правило валідації
"""

def getCountryName():
    user_input = input("Input the name of country: ")

    if (re.match(r"[A-B]{1}[a-b]{1-10}&", user_input)):
        return user_input
    else:
        return False
    #TODO



"""
    Написати валідатор ....
    Правило валідації
"""


def getDishName():
    user_input = input("Input the name of dish: ")

    if (re.match(r"[A-B]{1}[a-b]{1-10}&", user_input)):
        return user_input
    else:
        return False
    #TODO
getUserPassport()