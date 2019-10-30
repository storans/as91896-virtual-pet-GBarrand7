# Program to print a menu of available foods and their weight gain values and to allow the user to select a food for their cat to eat
# Setting the starting number for the numbered list
number = 1
# Using a 2D list to store the foods and their weight gain values
foods = [["salmon", 0.4], ["jelly meat", 0.3], ["biscuits", 0.2]]

# Printing the food menu
print("Here are the foods available and how much weight your cat will gain if it eats them:")
# Printing each food and it's corresponding weight gain value from the 2D list in a numbered list
for food in foods:
    print("{}. {} - {}".format(number, food[0], food[1]))
    # Increasing the number for the numbered list
    number += 1

# Setting valid to false in order to run the loop
valid = False
# Loop that runs until user enters a valid input
while valid == False:
    # Getting user input for which food they would like their cat to eat
    food_choice = int(input("Please enter the corresponding number to the food you would like your pet to eat >> "))
    # Providing feedback to the user based on their input and the food that that input corresponds to
    if food_choice == 1:
        print("You cat has eaten salmon and has gained {}kg".format(foods[0][1]))
        # Breaking the loop as user has entered a valid integer
        valid = True
    elif food_choice == 2:
        print("You cat has eaten jelly meat and has gained {}kg".format(foods[1][1]))
        # Breaking the loop as user has entered a valid integer
        valid = True
    elif food_choice == 3:
        print("You cat has eaten biscuits and has gained {}kg".format(foods[2][1]))
        # Breaking the loop as user has entered a valid integer
        valid = True
    # Branch which runs if the user has not entered a valid integer input which then loops back to ask the user for input again
    else:
        print("Please enter either 1, 2, or 3")
