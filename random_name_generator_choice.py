# Program to allow the user to select whether they want to have a name generated or to enter their own name

# Import random module

import random

# Function to randomly generate a name of a user selected gender
def name_generator(list, list_name, message):
    generate = ""
    while generate == "":
        name = random.choice(list_name[list])
        print(name)
        generate = input("{}".format(message))
    return name

# Using a 2D list to store the names for use if the user wants a randomly generated name
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender

names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]

valid = False
keep_going = ""
# Loop for testing purposes
while keep_going == "":
    print("It is time to name your cat! You have two options:")
    print("1. Choose your own name")
    print("2. Have a name randomly generated")
    while not valid:
        choice = int(input("Press either <1> or <2> to select how you want to name your cat >>"))


        if choice == 1:
            # Allowing the user to enter a name

            name = input("What would you like to name your cat? ")
            print("{} is a wonderful name!".format(name))
            valid = True
        elif choice == 2:
            # Asking what gender name the user would like
            gender = input("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name >>")
            if gender == "g":
                # Randomly generating a name from the girl's name list until the user says they like the name using the name_generator function
                name = name_generator(0, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
                print("Your cat's name is {}".format(name))
                valid = True
            elif gender == "b":
                # Randomly generating a name from the boy's name list until the user says they like the name using the name_generator function
                name = name_generator(1, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
                print("Your cat's name is {}".format(name))
                valid = True
            elif gender == "n":
                # Randomly generating a name from the gender neutral name list until the user says they like the name using the name_generator function
                name = name_generator(2, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
                print("Your cat's name is {}".format(name))
                valid = True
            else:
                print("Please enter either <g>, <b> or <n>")

        else:
            print("Please enter either 1 or 2")

    keep_going = input("Would you like to continue? Press <enter> to continue ")

