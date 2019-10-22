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

keep_going = ""
valid = False
# Loop for testing purposes
while keep_going == "":
    while valid == False:
        # Allowing user to select what exercise they want to do
        exercise_choice = int(input("Please enter the corresponding number to the exercise you would like your pet to do >> "))
        # Providing feedback based on the exercise chosen by the user
        if exercise_choice == 1:
            print("You cat has chased a mouse and has lost {}kg".format(EXERCISE["chase a mouse"]))
            valid = True
        elif exercise_choice == 2:
            print("You cat has climbed a tree and has lost {}kg".format(EXERCISE["climb a tree"]))
            valid = True
        elif exercise_choice == 3:
            print("You cat has scratched a post and has lost {}kg".format(EXERCISE["scratch a post"]))
            valid = True
        else:
            print("Please enter either 1, 2, or 3")
    keep_going = input("Press <enter> to continue")
    valid = False
