# Program to randomly generate a name from a dictionary
# Decided not to use this method as it was impractical and difficult to do compared to using the 2D list
# Importing random module

import random

# Trialling using a dictionary to store the names
# names = {"Pixie":"g", "Babushka":"g", "Poppy":"g", "Molly":"g", "Tina":"g", "Tinkerbell":"g", "Lord Meowsworth":"b", "Chad": "b", "Ernie": "b", "Clyde": "b", "Mr Cat": "b", "Garfield": "b", "Mittens": "n", "Fluffy": "n", "Hairball": "n", "Fleabag": "n", "Minty": "n", "Whiskers": "n", "Ginger": "n"}

# Dictionary of girls names
girls = {1: "Pixie", 2: "Babushka"}
# Dictionary of boys names
boys = {1: "Clyde", 2: "Garfield"}
# Dictionary of gender neutral names
neutral = {1: "Whiskers", 2: "Minty"}
# List of numbers corresponding to names - only need one list at present as there is the same number of each type of name
numbers = [1, 2]

# Loop for testing
for i in range(3):
    gender = input("What type of name would you like? For a girl's name type <g>, for a boy's name type <b> or for a gender neutral name type <n>")
    # Randomly generating a number which will correspond to a name
    number = random.choice(numbers)
    # Generating a name if the user wants a girl's name
    if gender == "g":
        name = girls[number]
        print(name)
    # Generating a name if the user wants a boy's name
    elif gender == "b":
        name = boys[number]
        print(name)
    # Generating a name if the user wants a gender neutral name
    else:
        name = neutral[number]
        print(name)


