# Program to allow the user to generate a random name
# Function to randomly generate a name of a user selected gender
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

# Using a 2D list to store the names
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender
names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]

# Variable which allows a continuous loop for testing
keep_going = ""
# setting variable to run loop while valid is equal to false
valid = False

# Loop for testing purposes
while keep_going == "":
    # Loop runs until user enters a valid input
    while valid == False:
        # Asking what gender name the user would like
        gender = input("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name >>")
        if gender == "g":
            # Randomly generating a name from the girl's name list until the user says they like the name using the name_generator function
            name = name_generator(0, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
            print("Your cat's name is {}".format(name))
            # Breaking loop as user has entered a valid input
            valid = True
        elif gender == "b":
            # Randomly generating a name from the boy's name list until the user says they like the name using the name_generator function
            name = name_generator(1, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
            print("Your cat's name is {}".format(name))
            # Breaking loop as user has entered a valid input
            valid = True
        elif gender == "n":
            # Randomly generating a name from the gender neutral name list until the user says they like the name using the name_generator function
            name = name_generator(2, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
            print("Your cat's name is {}".format(name))
            # Breaking loop as user has entered a valid input
            valid = True
        # Branch which runs if user has not entered an expected input
        else:
            print("Please enter either <g>, <b> or <n>")

    # Checking to see if the user would like to continue testing or end the loop
    keep_going = input("Would you like to keep going? Press <enter> to continue")
