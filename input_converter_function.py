# Import random module

import random

def name_generator(list_segment, list_name, message):
    generate = ""
    while generate == "":
        name = random.choice(list_name[list_segment])
        print(name)
        generate = input("{}".format(message))
    return name

def input_converter(question, error):
    valid = False
    while valid == False:
        gender = input(question)
        if gender in genders[0]:
            gender = "g"
            return gender
        elif gender in genders[1]:
            gender = "b"
            return gender
        elif gender in genders[2]:
            gender = "n"
            return gender
        else:
            print(error)

genders = [['g', 'girl', 'f', 'female'], ['b', 'boy', 'male', 'm'], ['n', 'neutral', 'gn', 'gender neutral']]
yes = ['yes', 'y']
no = ['no', 'n']
# Using a 2D list to store the names
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender
names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]

# Variable which allows a continuous loop for testing
keep_going = ""

# Loop for testing purposes
while keep_going == "":
    gender  = input_converter("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name >>", "Please enter either <g>, <b> or <n>")
    if gender == "g":
        # Randomly generating a name from the girl's name list until the user says they like the name using the name_generator function
        name = name_generator(0, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
        print("Your cat's name is {}".format(name))
    elif gender == "b":
        # Randomly generating a name from the boy's name list until the user says they like the name using the name_generator function
        name = name_generator(1, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
        print("Your cat's name is {}".format(name))
    elif gender == "n":
        # Randomly generating a name from the gender neutral name list until the user says they like the name using the name_generator function
        name = name_generator(2, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name")
        print("Your cat's name is {}".format(name))

    # Checking to see if the user would like to continue testing or end the loop
    keep_going = input("Would you like to keep going? Press <enter> to continue")

