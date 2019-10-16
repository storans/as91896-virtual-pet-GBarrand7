# Program to allow the user to generate a random name

# Import random module

import random

# Trialling using a 2D list to store the names
# First list holds girls' names, second list holds boys' names and third list hold names which could be either gender
names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]
numbers = [0, 1, 2]

for i in range(5):
    number = random.choice(numbers)
    print(number)
    name = random.choice(names[number])
    print(name)
