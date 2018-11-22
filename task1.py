from data import dataset

#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Викликати функцію


def addUserDish(user_name, country, dish):
    if user_name in dataset:
        if country in user_name:
            dataset[user_name][country].add(dish)
        else:
            dataset[user_name][country]={dish}           #={country:{dish}}
    else:
        dataset[user_name]={country:{dish}}

    #TODO



print("Task 1")

#Додати нового користувача та страву у новій країні
addUserDish("EK346743","USA","Water")

#Додати існуючому користувачу нову країну з новою стравою
addUserDish("PS334743","Ukraine","Water")

#Додати існуючому користувачу нову страву в існуючого країну
addUserDish("EK346743","Ukraine","Kovbasa")

print(dataset)


print("\n\n")