# Program to convert user input to the expected value when they enter a gender
# Import random module

import random

# Function to randomly generate a name
# Parameters - list_segment - what part of the 2D list the name is generated from based on the desired gender, list_name - the list the names are stored in, message - asking the user if they like the name or not
def name_generator(list_segment, list_name, message):
    # Setting the generate variable
    generate = ""
    # Names are generated while generate = ""
    while generate == "":
        # Randomly generating a name for the chosen gender
        name = random.choice(list_name[list_segment])
        print(name)
        # Setting valid to false to run the loop
        valid = False
        # Loop runs until user enters a valid input for yes or no
        while valid == False:
            # Asking if the user likes the name generated
            generate = input("{}".format(message)).strip().lower()
            # Converting the affirmative inputs into the desired input
            if generate in ["yes", "yeah", "y", "sure"]:
                generate = "yes"
                valid = True
            # Converting the negative inputs into the desired input
            elif generate in ["no", "n", "nah", ""]:
                generate = ""
                valid = True
            # Branch which runs if the user does not enter any expected input which then loops back to ask the user for input again
            else:
                print("Please enter either yes or no")
    # Returning the approved name for use in the program
    return name

# Function to convert user's gender input to the desired input if their input is within an approved list
# Parameters - question - the question asked, error - the error message if the user enters none of the desired inputs
def input_converter(question, error):
    # Setting valid to False
    valid = False
    # Function asks for input until the user inputs a valid response
    while valid == False:
        # Asking user for input as to what gender name they would like
        gender = input(question).strip().lower()
        # Checking if the gender is within the approved list of inputs for female gender
        if gender in genders[0]:
            # Changing input to the standard input
            gender = "g"
            # Returning the correct form of the desired gender
            return gender
        # Checking if the gender is within the approved list of inputs for male gender
        elif gender in genders[1]:
            # Changing input to the standard input
            gender = "b"
            # Returning the correct form of the desired gender
            return gender
        # Checking if the gender is within the approved list of inputs for gender neutral
        elif gender in genders[2]:
            # Changing input to the standard input
            gender = "n"
            # Returning the correct form of the desired gender
            return gender
        # Branch which runs if the user does not enter any expected input
        else:
            print(error)

# 2D list of expected inputs for each gender
genders = [['g', 'girl', 'f', 'female'], ['b', 'boy', 'male', 'm'], ['n', 'neutral', 'gn', 'gender neutral']]

# Using a 2D list to store the names
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender
names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]

# Variable which allows a continuous loop for testing
keep_going = ""

# Loop for testing purposes
while keep_going == "":
    # Asking user for input as to what gender name they would like
    gender = input_converter("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name >>", "Please enter either <g>, <b> or <n>")
    # Branch which runs if the user has selected a girl's name
    if gender == "g":
        # Randomly generating a name from the girl's name list until the user says they like the name using the name_generator function
        name = name_generator(0, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
        print("Your cat's name is {}".format(name))
    # Branch which runs if the user has selected a boy's name
    elif gender == "b":
        # Randomly generating a name from the boy's name list until the user says they like the name using the name_generator function
        name = name_generator(1, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
        print("Your cat's name is {}".format(name))
    # Branch which runs if the user has selected a gender neutral name
    elif gender == "n":
        # Randomly generating a name from the gender neutral name list until the user says they like the name using the name_generator function
        name = name_generator(2, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
        print("Your cat's name is {}".format(name))

    # Checking to see if the user would like to continue testing or end the loop
    keep_going = input("Would you like to keep going? Press <enter> to continue")

