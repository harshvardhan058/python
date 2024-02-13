pet = "Dog"
age = 5

if pet == "Dog":
    if age < 2:
        food = "Puppy Dog food"
    else:
        food = "Senior Dog food"
elif pet == "Cat":
    if age < 5:
        food = "Puppy Cat food"
    else:
        food = "Senior Cat food"
else:
    print("We Don't Data for Your Pet")
    exit()

print("Your",pet,"of Age",age,"Should eat",food)