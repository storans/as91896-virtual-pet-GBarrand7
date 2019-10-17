# Program to allow the user to generate a random name

# Import random module

import random

# Trialling using a 2D list to store the names
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender
names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]

keep_going = ""

while keep_going == "":
    gender = input("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name >>")
    if gender == "g":
        # Randomly generating a name from the girl's name list
        name = random.choice(names[0])
    elif gender == "b":
        # Randomly generating a name from the boy's name list
        name = random.choice(names[1])
    elif gender == "n":
        # Randomly generating a name from the neutral names list
        name = random.choice(names[2])

    print("Your cat's name is {}".format(name))

    keep_going = input("Would you like to keep going? Press <enter> to continue")
