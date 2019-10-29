FOODS = {"salmon": 0.4, "jelly meat": 0.3, "biscuits": 0.2}
# Starting number for numbered list
number = 1
print("Here are the foods available and how much weight your cat will gain if it eats them:")
for food, amount in FOODS.items():
    print("{}. {} - {}".format(number, food, amount))
    number += 1

valid = False
# Loop that runs until user enters a valid input
while valid == False:
    food_choice = int(input("Please enter the corresponding number to the food you would like your pet to eat >> "))
    if food_choice == 1:
        print("You cat has eaten salmon and has gained {}kg".format(FOODS["salmon"]))
        valid = True
    elif food_choice == 2:
        print("You cat has eaten jelly meat and has gained {}kg".format(FOODS["jelly meat"]))
        valid = True
    elif food_choice == 3:
        print("You cat has eaten biscuits and has gained {}kg".format(FOODS["biscuits"]))
        valid = True
    else:
        print("Please enter either 1, 2, or 3")

