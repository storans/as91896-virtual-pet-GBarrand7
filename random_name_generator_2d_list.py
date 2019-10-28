# Program to allow the user to generate a random name

# Import random module

import random

# Trialling using a 2D list to store the names
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender
names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]

# Variable which holds whether the user likes the generated name or not
like = ""
# Variable which allows a continuous loop for testing
keep_going = ""

# Loop for testing purposes
while keep_going == "":
    # Asking what gender name the user would like
    gender = input("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name >>")
    if gender == "g":
        # Randomly generating a name from the girl's name list until the user says they like the name
        while like == "":
            name = random.choice(names[0])
            print(name)
            # Asking whether the user likes the name or not
            like = input("Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
            # Once the user says they like the name the name is printed
            if like == "yes":
                print("Your cat's name is {}".format(name))
    elif gender == "b":
        # Randomly generating a name from the boy's name list until the user says they like the name
        while like == "":
            name = random.choice(names[1])
            print(name)
            # Asking whether the user likes the name or not
            like = input("Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
            # Once the user says they like the name the name is printed
            if like == "yes":
                print("Your cat's name is {}".format(name))
    elif gender == "n":
        # Randomly generating a name from the gender neutral name list until the user says they like the name
        while like == "":
            name = random.choice(names[2])
            print(name)
            # Asking whether the user likes the name or not
            like = input("Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
            # Once the user says they like the name the name is printed
            if like == "yes":
                print("Your cat's name is {}".format(name))

    else:
        print("Please enter either <g>, <b> or <n>")

    keep_going = input("Would you like to keep going? Press <enter> to continue")
    like = ""
