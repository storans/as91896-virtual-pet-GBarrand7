# Program to check if user's input is a number and within a certain range - used for exercise and food menus

# Function to check if a integer is between two values
# Parameters:
# high - highest possible value
# low - lowest possible value
# error_1 - error message for if the user enters an integer outside of the range
# error_2 - error message for if the user does not enter an integer
# question - the question which asks for the user's input
def integer_checker(high, low, error_1, error_2, question):
    # Setting valid to false to run the loop
    valid = False
    # Loop runs until user enters a valid input
    while valid == False:
        # Checking if the user has entered an integer
        try:
            # Asking for user's response to the question
            response = int(input("{} >> ".format(question)))
            # Checking if the user's response is within the desired range
            if low <= response <= high:
                # Returning response for use in program
                return response
            # Branch which runs if the user has entered an integer outside of the desired range
            else:
                print(error_1)
        # Branch which runs if the user has not entered an integer
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

# Variable for continual testing
keep_going = ""

# Loop for testing purposes
while keep_going == "":
    # Allowing user to select what exercise they want to do and checking that their input is within the desired range
    exercise_choice = integer_checker(3, 1, "Please enter either 1, 2, or 3", "Please enter either 1, 2, or 3",  "Please enter the corresponding number to the exercise you would like your pet to do")
    # Providing feedback based on the exercise chosen by the user
    if exercise_choice == 1:
        print("Your cat has chased a mouse and has lost {}kg".format(EXERCISE["chase a mouse"]))
    elif exercise_choice == 2:
        print("Your cat has climbed a tree and has lost {}kg".format(EXERCISE["climb a tree"]))
    elif exercise_choice == 3:
        print("Your cat has scratched a post and has lost {}kg".format(EXERCISE["scratch a post"]))
    keep_going = input("Press <enter> to continue")


