# Program to print the exercise menu and allow the user to choose an exercise from it for their pet to do
# Dictionary of possible exercises
EXERCISE={"chase a mouse": 0.4, "climb a tree": 0.3, "scratch a post": 0.2}
# Starting value for numbered list
number = 1
print("Here are the exercises your cat can do and how much weight it will lose if it does them: ")
# Getting the exercise and its corresponding weight loss amount from the dictionary and printing it in a formatted way
for activity, amount in EXERCISE.items():
    print("{}. {} - {}".format(number, activity, amount))
    # Increasing number for numbered list
    number += 1

# Setting variable to continue loop for testing
keep_going = ""
# Setting valid to false in order to run the loop that asks for input until a valid input is entered
valid = False
# Loop for testing purposes
while keep_going == "":
    # Loop that asks for input until a valid input is entered
    while valid == False:
        # Allowing user to select what exercise they want to do
        exercise_choice = int(input("Please enter the corresponding number to the exercise you would like your pet to do >> "))
        # Providing feedback based on the exercise chosen by the user
        if exercise_choice == 1:
            print("You cat has chased a mouse and has lost {}kg".format(EXERCISE["chase a mouse"]))
            # Breaking the valid loop as the user has entered a valid input
            valid = True
        elif exercise_choice == 2:
            print("You cat has climbed a tree and has lost {}kg".format(EXERCISE["climb a tree"]))
            # Breaking the valid loop as the user has entered a valid input
            valid = True
        elif exercise_choice == 3:
            print("You cat has scratched a post and has lost {}kg".format(EXERCISE["scratch a post"]))
            # Breaking the valid loop as the user has entered a valid input
            valid = True
        # Branch which runs if the user enters a number outside of the desired range
        else:
            print("Please enter either 1, 2, or 3")
    # Getting input to either continue or exit the testing loop
    keep_going = input("Press <enter> to continue")
    # Setting valid to false so that the loop still runs when doing continual testing
    valid = False
