# Program to allow the user to generate a random name

# Import random module

import random

# Trialling using a 2D list to store the names
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender
names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]
# List of numbers which will be randomly selected from in order to select a list from names
numbers = [0, 1, 2]

# Loop for testing
for i in range(5):
    # Randomly generating a number which corresponds to a list in names
    number = random.choice(numbers)
    print(number)
    # Randomly generating a name from the selected list
    name = random.choice(names[number])
    print(name)
