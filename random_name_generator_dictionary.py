#Importing random module

import random

# Trialling using a dictionary to store the names
# names = {"Pixie":"g", "Babushka":"g", "Poppy":"g", "Molly":"g", "Tina":"g", "Tinkerbell":"g", "Lord Meowsworth":"b", "Chad": "b", "Ernie": "b", "Clyde": "b", "Mr Cat": "b", "Garfield": "b", "Mittens": "n", "Fluffy": "n", "Hairball": "n", "Fleabag": "n", "Minty": "n", "Whiskers": "n", "Ginger": "n"}
names = {"g": "Pixie", "g": "Babushka", "b": "Clyde", "b": "Garfield", "n": "Whiskers", "n": "Minty"}

# List of available genders
genders = ["g", "b", "n"]

# Loop for testing
for i in range(5):
    gender = random.choice(genders)
    name = random.choice(names[gender])

