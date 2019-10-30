# Program to print the exercise menu and allow the user to choose an exercise from it for their pet to do
# 2D list of exercises and their weight loss value
exercises = [["chase a mouse", 0.4], ["climb a tree", 0.3], ["scratch a post", 0.2]]

# Setting the starting number for the numbered list
number = 1

print("Here are the exercises available and how much weight your cat will lose if it does them:")
# Printing each food and it's corresponding weight gain value from the 2D list in a numbered list
for exercise in exercises:
    print("{}. {} - {}".format(number, exercise[0], exercise[1]))
    # Increasing the number for the numbered list
    number += 1
# Setting valid to false to run the loop
valid = False
# Asking for input until user enters a valid input
while valid == False:
    # Allowing user to select what exercise they want to do
    exercise_choice = int(input("Please enter the corresponding number to the exercise you would like your pet to do >> "))
    # Providing feedback based on the exercise chosen by the user
    if exercise_choice == 1:
        print("You cat has chased a mouse and has lost {}kg".format(exercises[0][1]))
        # Breaking the loop as user has entered a valid input
        valid = True
    elif exercise_choice == 2:
        print("You cat has climbed a tree and has lost {}kg".format(exercises[1][1]))
        # Breaking the loop as user has entered a valid input
        valid = True
    elif exercise_choice == 3:
        print("You cat has scratched a post and has lost {}kg".format(exercises[2][1]))
        # Breaking the loop as user has entered a valid input
        valid = True
    # Branch which runs if the user enters an integer outside of the desired range
    else:
        print("Please enter either 1, 2 or 3")
