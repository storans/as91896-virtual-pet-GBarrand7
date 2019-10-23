# Function to generate a menu

# Menu generator for list stored data
# Parameters - list is the list the data is stored in and starting_message is the message wanted before the list
def menu_generator(list, starting_message):
    # Starting number for numbered list
    number = 1
    print(starting_message)
    for item in list:
        print("{}. {}".format(number, item))
        number += 1

# List of wanted values for the home menu
home = ["Exercise your cat", "Feed your cat", "Check your cat's weight", "See the game instructions", "Quit"]
menu_generator(home, "Hello, and welcome to the virtual cat simulator!\n"
      "In this game you can name your cat, feed it and exercise it.\nBut, be careful!\nIf your cat gets too skinny or too fat it can die, so make sure your cat stays in a healthy weight range of 3.5-4.5kg.\nWe hope you enjoy the game!")
