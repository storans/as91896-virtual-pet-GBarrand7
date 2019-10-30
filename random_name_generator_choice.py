# Program to allow the user to select whether they want to have a name generated or to enter their own name

# Import random module

import random

# Function to randomly generate a name of a user selected gender
# Parameters:
# list - what list in the 2D list is wanted
# list_name - the name of the 2D list
# message - question to ask for input from the user
def name_generator(list, list_name, message):
    # Setting variable to run the loop
    generate = ""
    # Loop runs until user says they like the name
    while generate == "":
        # Name is generated from the list of names for a specified gender
        name = random.choice(list_name[list])
        print(name)
        # Getting input from the user to either break or continue the loop
        generate = input("{}".format(message))
    return name

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

# Using a 2D list to store the names for use if the user wants a randomly generated name
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender

names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]

# Setting variable to run loop for testing
keep_going = ""
# Loop for testing purposes
while keep_going == "":
    # Showing user a menu of their choices
    print("It is time to name your cat! You have two options:")
    print("1. Choose your own name")
    print("2. Have a name randomly generated")
    # Getting users choice for how they want to name their cat and running it through the integer checker to make sure it's valid
    choice = integer_checker(2, 1, "Please enter either 1 or 2", "Please enter either 1 or 2", "Press either <1> or <2> to select how you want to name your cat")

    # User chooses to enter their own name
    if choice == 1:
        # Allowing the user to enter a name
        name = input("What would you like to name your cat? ")
        print("{} is a wonderful name!".format(name))
    # User chooses to randomly generate a name
    elif choice == 2:
        # Asking what gender name the user would like
        gender = input("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name >>")
        if gender == "g":
            # Randomly generating a name from the girl's name list until the user says they like the name using the name_generator function
            name = name_generator(0, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
            print("Your cat's name is {}".format(name))
        elif gender == "b":
            # Randomly generating a name from the boy's name list until the user says they like the name using the name_generator function
            name = name_generator(1, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
            print("Your cat's name is {}".format(name))
        elif gender == "n":
            # Randomly generating a name from the gender neutral name list until the user says they like the name using the name_generator function
            name = name_generator(2, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
            print("Your cat's name is {}".format(name))

    # Getting input to see if the user wants to continue testing
    keep_going = input("Would you like to continue? Press <enter> to continue ")

