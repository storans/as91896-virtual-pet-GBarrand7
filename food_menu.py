FOODS = {"salmon": 0.4, "jelly meat": 0.3, "biscuits": 0.2}
# Starting number for numbered list
number = 1
print("Here are the foods available and how much weight your cat will gain if it eats them:")
for food, amount in FOODS.items():
    print("{}. {} - {}".format(number, food, amount))
    number += 1

# Loop for testing purposes
for i in range(3):
    food_choice = int(input("Please enter the corresponding number to the food you would like your pet to eat >> "))
    if food_choice == 1:
        print("You cat has eaten salmon and has gained {}kg".format(FOODS["salmon"]))
    elif food_choice == 2:
        print("You cat has eaten jelly meat and has gained {}kg".format(FOODS["jelly meat"]))
    elif food_choice == 3:
        print("You cat has eaten biscuits and has gained {}kg".format(FOODS["biscuits"]))

