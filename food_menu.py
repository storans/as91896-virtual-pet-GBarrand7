# Program to print a menu of available foods and their weight gain values and to allow the user to select a food for their cat to eat
# Using a dictionary to store the foods and their corresponding weight gain values
FOODS = {"salmon": 0.4, "jelly meat": 0.3, "biscuits": 0.2}
# Starting number for numbered list
number = 1
print("Here are the foods available and how much weight your cat will gain if it eats them:")
# Printing each food and their corresponding weight loss values in a formatted numbered list
for food, amount in FOODS.items():
    print("{}. {} - {}".format(number, food, amount))
    # Increasing the number for the numbered list
    number += 1

# Setting valid to false in order to run the loop
valid = False
# Loop that runs until user enters a valid input
while valid == False:
    # Asking for users input to select which food they would like
    food_choice = int(input("Please enter the corresponding number to the food you would like your pet to eat >> "))
    # Providing feedback as to what the user's cat has done based on their food choice
    if food_choice == 1:
        print("You cat has eaten salmon and has gained {}kg".format(FOODS["salmon"]))
        # Breaking the loop as the user has entered a valid integer
        valid = True
    elif food_choice == 2:
        print("You cat has eaten jelly meat and has gained {}kg".format(FOODS["jelly meat"]))
        # Breaking the loop as the user has entered a valid integer
        valid = True
    elif food_choice == 3:
        print("You cat has eaten biscuits and has gained {}kg".format(FOODS["biscuits"]))
        # Breaking the loop as the user has entered a valid integer
        valid = True
    # Branch which runs if the user does not enter a valid integer and then loops back to ask the user for input again
    else:
        print("Please enter either 1, 2, or 3")

