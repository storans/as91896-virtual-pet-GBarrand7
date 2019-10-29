# Setting the starting number for the numbered list
number = 1
# 2D list of foods and their weight gain value
foods = [["salmon", 0.4], ["jelly meat", 0.3], ["biscuits", 0.2]]

print("Here are the foods available and how much weight your cat will gain if it eats them:")
# Printing each food and it's corresponding weight gain value from the 2D list in a numbered list
for food in foods:
    print("{}. {} - {}".format(number, food[0], food[1]))
    # Increasing the number for the numbered list
    number += 1

valid = False
# Loop that runs until user enters a valid input
while valid == False:
    food_choice = int(input("Please enter the corresponding number to the food you would like your pet to eat >> "))
    if food_choice == 1:
        print("You cat has eaten salmon and has gained {}kg".format(foods[0][1]))
        valid = True
    elif food_choice == 2:
        print("You cat has eaten jelly meat and has gained {}kg".format(foods[1][1]))
        valid = True
    elif food_choice == 3:
        print("You cat has eaten biscuits and has gained {}kg".format(foods[2][1]))
        valid = True
    else:
        print("Please enter either 1, 2, or 3")
