# Program to check if user's input is a number and within a certain range - used for exercise and food menus

# Function to check if a integer is between two values
def integer_checker(high, low, error_1, error_2, question):
    valid = False
    while valid == False:
        try:
            response = int(input("{} >> ".format(question)))
            if low <= response <= high:
                return response
            else:
                print(error_1)
        except ValueError:
            print(error_2)

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
    # Allowing user to select what exercise they want to do
    exercise_choice = integer_checker(3, 1, "Please enter either 1, 2, or 3", "Please enter either 1, 2, or 3",  "Please enter the corresponding number to the exercise you would like your pet to do")
    # Providing feedback based on the exercise chosen by the user
    if exercise_choice == 1:
        print("Your cat has chased a mouse and has lost {}kg".format(EXERCISE["chase a mouse"]))
    elif exercise_choice == 2:
        print("Your cat has climbed a tree and has lost {}kg".format(EXERCISE["climb a tree"]))
    elif exercise_choice == 3:
        print("Your cat has scratched a post and has lost {}kg".format(EXERCISE["scratch a post"]))
    keep_going = input("Press <enter> to continue")
