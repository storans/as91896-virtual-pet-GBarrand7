# Function to generate a menu

# Menu generator for list stored data
# Parameters - list is the list the data is stored in and starting_message is the message wanted before the list
def menu_generator_list(list, starting_message):
    # Starting number for numbered list
    number = 1
    print(starting_message)
    for item in list:
        print("{}. {}".format(number, item))
        number += 1

def menu_generator_dict(dictionary, starting_message):
    # Starting number for numbered list
    number = 1
    print(starting_message)
    for first, second in dictionary.items():
        print("{}. {} - {}".format(number, first, second))
        number += 1

# List of wanted values for the home menu
home = ["Exercise your cat", "Feed your cat", "Check your cat's weight", "See the game instructions", "Quit"]
menu_generator_list(home, "Hello, and welcome to the virtual cat simulator!\n"
      "In this game you can name your cat, feed it and exercise it.\nBut, be careful!\nIf your cat gets too skinny or too fat it can die, so make sure your cat stays in a healthy weight range of 3.5-4.5kg.\nWe hope you enjoy the game!")

# Dictionary of possible exercises
EXERCISE={"Chase a mouse": 0.4, "Climb a tree": 0.3, "Scratch a post": 0.2}
print("")
menu_generator_dict(EXERCISE, "Here are the exercises your cat can do and how much weight it will lose if it does them: ")

# Dictionary of possible foods
FOODS = {"salmon": 0.4, "jelly meat": 0.3, "biscuits": 0.2}
print("")
menu_generator_dict(FOODS, "Here are the foods your cat can eat and how much weight it will gain if it eats them: ")
