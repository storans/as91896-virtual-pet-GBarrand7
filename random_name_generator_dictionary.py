#Importing random module

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
    number = random.choice(numbers)
    if gender == "g":
        name = girls[number]
        print(name)
    elif gender == "b":
        name = boys[number]
        print(name)
    else:
        name = neutral[number]
        print(name)


