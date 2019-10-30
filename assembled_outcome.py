# First version of assembled outcome
# Import random module for use throughout the program to randomly generate various things - e.g names

import random

# Function to randomly generate a name
# Parameters - list_segment - what part of the 2D list the name is generated from based on the desired gender, list_name - the list the names are stored in, message - asking the user if they like the name or not
def name_generator(list_segment, list_name, message):
    # Setting the generate variable to ""
    generate = ""
    # Names are generated while generate = ""
    while generate == "":
        # Randomly generating a name for the chosen gender
        name = random.choice(list_name[list_segment])
        # Printing the randomly generated name
        print(name)
        # Setting valid to False in order to run the loop
        valid = False
        # Loop runs while valid == False
        while valid == False:
            # Asking if the user likes the name generated and making the input lowercase and removing any spaces before or after
            generate = input("{}".format(message)).strip().lower()
            # Converting the affirmative inputs into the desired input
            if generate in ["yes", "yeah", "y", "sure"]:
                # Breaking generate loop by setting it to "yes"
                generate = "yes"
                # Breaking valid loop by setting it to True
                valid = True
            # Converting the negative inputs into the desired input
            elif generate in ["no", "n", "nah", ""]:
                # Continuing generate loop so that another name is generated
                generate = ""
                # Setting valid to true to break the loop instead of repeatedly asking if the user likes the name
                valid = True
            # Branch that runs if the user enters an invalid input for generate
            else:
                print("Please enter either yes or no")
    # Returning the selected randomly generated name
    return name

# Function to convert user's gender input to the desired input if their input is within an approved list
# Parameters - question - the question asked, error - the error message if the user enters none of the desired inputs
def input_converter(question, error):
    # Setting valid to False
    valid = False
    # Function asks for input until the user inputs a valid response
    while valid == False:
        # Asking user what gender name they would like and making the input lowercase and removing any spaces before or after
        gender = input("{} >> ".format(question)).strip().lower()
        # Checking if the gender is within the approved list of inputs for female gender
        if gender in genders[0]:
            # Changing input to the standard input
            gender = "g"
            return gender
        # Checking if the gender is within the approved list of inputs for male gender
        elif gender in genders[1]:
            # Changing input to the standard input
            gender = "b"
            return gender
        # Checking if the gender is within the approved list of inputs for gender neutral
        elif gender in genders[2]:
            # Changing input to the standard input
            gender = "n"
            return gender
        # Branch which runs if the user does not enter any valid input for gender
        else:
            print(error)

# Functions to increase or decrease the cat's weight

# Parameters - amount specifies the amount of weight to be added or subtracted, weight specifies the weight of the cat
# Function to increase the cat's weight
def add(amount, weight):
    # Adding both parameters together
    weight += amount
    return weight

# Function to decrease the cat's weight
def subtract(amount, weight):
    # Subtracting the specific amount from the cat's current weight
    weight -= amount
    return weight

# Function to check if the cat has died or is near death
# Parameters - new_weight is the cat's weight after being feed or exercised, low is the lowest possible weight the cat can be, high is the highest possible weight the cat can be, boundary is the bracket within which the cat is near being overweight or underweight
def death_checker(new_weight, low, high, boundary):
    # Messages for if the cat has died from being too overweight or too underweight, or if they are near being too underweight or overweight
    too_high = "Unfortunately, your cat has eaten too much and has passed away. Make sure to exercise your cat more next time."
    too_low = "Unfortunately, your cat has not eaten enough and has passed away. Make sure to feed your cat more next time."
    near_low = "Make sure to feed your cat soon!"
    near_high = "Make sure to exercise your cat soon!"
    # If cat's weight is below the lowest weight
    if new_weight < low:
        print(too_low)
        # Setting cat's weight to "dead" and returning this for use in the program
        new_weight = "dead"
        return new_weight
    # If cat's weight is above the highest weight
    elif new_weight > high:
        print(too_high)
        # Setting cat's weight to "dead" and returning this for use in the program
        new_weight = "dead"
        return new_weight
    # If cat's weight is between the lowest weight and a weight near the lowest weight (e.g 3.5 - 3.8)
    elif low <= new_weight <= (low + boundary):
        print(near_low)
        return new_weight
    # If cat's weight is below the highest weight and a weight near the highest weight (e.g 4.2 - 4.5
    elif high >= new_weight >= (high - boundary):
        print(near_high)
        return new_weight
    # If the cat is in a healthy weight range
    else:
        return new_weight

# Functions to generate a menu

# Menu generator for list stored data
# Parameters - list is the list the data is stored in and starting_message is the message wanted before the numbered list
def menu_generator_list(list, starting_message):
    # Starting number for numbered list
    number = 1
    print(starting_message)
    # Printing each item in the list in a formatted way
    for item in list:
        print("{}. {}".format(number, item))
        # Increasing the number for the numbered list
        number += 1

# Menu generator for dictionary stored data
# Parameters - dictionary - the dictionary name where the data is stored, starting_message - the message wanted before the numbered list
def menu_generator_dict(dictionary, starting_message):
    # Starting number for numbered list
    number = 1
    print(starting_message)
    # Printing each key and value in the dictionary in a formatted form
    for first, second in dictionary.items():
        print("{}. {} - {}kg".format(number, first, second))
        # Increasing the number for the numbered list
        number += 1

# Function to check if a float is between two values
# Parameters - high is the highest possible value, low is the lowest possible value, error_1 is the error for if the user has entered a number outside of the range, error_2 is the error for if the user hasn't entered a number
# Question is the question being asked of the user
def float_checker(high, low, error_1, error_2, question):
    # Setting valid to false to run the loop
    valid = False
    # Loop runs while valid is false so the question is asked until a valid answer is entered
    while valid == False:
        try:
            # Getting the user's response
            response = float(input("{:.1f} >> ".format(question)))
            # If the response entered is a number within the designated range then the response is returned
            if low <= response <= high:
                return response
            # If the response is outside of the range then the first error message is displayed
            else:
                print(error_1)
        # If the user does not enter a number then the second error is displayed
        except ValueError:
            print(error_2)

# Function to check if a integer is between two values
# Parameters - high is the highest possible value, low is the lowest possible value, error_1 is the error for if the user has entered a number outside of the range, error_2 is the error for if the user hasn't entered a number
# Question is the question being asked of the user
def integer_checker(high, low, error_1, error_2, question):
    # Setting valid to false to run the loop
    valid = False
    # Loop runs while valid is false so the question is asked until a valid answer is entered
    while valid == False:
        try:
            # Getting the user's response
            response = int(input("{} >> ".format(question)))
            # If the user has entered an integer within the range then the response is returned
            if low <= response <= high:
                return response
            # If the user has entered an integer outside of the range then the first error is displayed
            else:
                print(error_1)
        # If the user has not entered an integer then the second error is displayed
        except ValueError:
            print(error_2)

# 2D list of possible gender inputs
genders = [['g', 'girl', 'f', 'female'], ['b', 'boy', 'male', 'm'], ['n', 'neutral', 'gn', 'genderneutral']]

# Start of game

print("Hello, and welcome to the virtual cat simulator!\n"
      "In this game you can name your cat, feed it and exercise it.\nBut, be careful!\nIf your cat gets too skinny or too fat it can die, so make sure your cat stays in a healthy weight range of 3.5-4.5kg.\nWe hope you enjoy the game!")

# List to store possible options on the numbered list of the name generator menu
name_choice = ["Choose your own name", "Have a name randomly generated"]
# Generating a menu to show the user the options they have for selecting a name
menu_generator_list(name_choice, "First, let's name your cat. You have two options: ")

# Allowing user to make their choice for how to name their pet
choice = integer_checker(2, 1, "Please enter either 1 or 2", "Please enter either 1 or 2", "Press either <1> or <2> to select how you want to name your cat")
# If user chooses to enter their own name
if choice == 1:
    # Allowing the user to enter a name
    name = input("What would you like to name your cat? ").title()
    print("{} is a wonderful name!".format(name))

# If user chooses to have a name generated for them
elif choice == 2:
    # Using a 2D list to store the names
    # First list holds girls' names, second list holds boys' names and third list hold names which could be either gender
    names = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"], ["Lord Meowsworth", "Chad", "Ernie", "Clyde", "Mr Cat", "Garfield"], ["Mittens", "Fluffy", "Hairball", "Fleabag", "Minty", "Whiskers", "Ginger"]]

    # Allowing user to choose what gender name they would like
    gender = input_converter("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name", "Please enter either <g>, <b> or <n>")
    # If user chooses that they want a girl's name
    if gender == "g":
        # Randomly generating a name from the girl's name list until the user says they like the name using the name_generator function
        name = name_generator(0, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
        print("Your cat's name is {}".format(name))
    # If user chooses that they want a boy's name
    elif gender == "b":
        # Randomly generating a name from the boy's name list until the user says they like the name using the name_generator function
        name = name_generator(1, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
        print("Your cat's name is {}".format(name))
    # If user chooses that they want a gender neutral name
    elif gender == "n":
        # Randomly generating a name from the gender neutral name list until the user says they like the name using the name_generator function
        name = name_generator(2, names, "Do you like this name? Type 'yes' to choose this name or press <enter> to generate another name >> ")
        print("Your cat's name is {}".format(name))

# Allowing user to choose their cat's starting weight
weight = float_checker(4.5, 3.5, "Please enter a weight between 3.5kg - 4.5kg", "Please enter a number", "Now, you can choose {}'s starting weight. Please pick a weight between 3.5 - 4.5kg".format(name))
# Informing user of their cat's weight and reminding them of the rules and then showing them a cat graphic
print("{} weighs {}kg. Make sure to keep {} within a healthy weight range of 3.5 - 4.5kg".format(name, weight, name))
print("Here is your cat {}!\n      \    /\\\n       )  ( ')\n      (  /  )\n       \(__)|".format(name))
# Home Menu
# List of wanted values for the home menu in the numbered list
home = ["Exercise your cat", "Feed your cat", "Check your cat's weight", "See the game instructions", "Quit"]
# Generating the home menu
menu_generator_list(home, "You are now set up to play Virtual Cat Simulator! We hope you enjoy the game!\n \nHOME MENU")

# Setting generate to false
generate = False

# Loop runs while generate is equal to false
while not generate:
    # Getting user's choice of activity from the menu and checking that it is within the wanted range
    activity_choice = integer_checker(5, 1, "Please enter a number between 1-5", "Please enter a number between 1-5", "What would you like to do? Select the corresponding number from the menu above")
    # User chooses to exercise their cat
    if activity_choice == 1:
        print("Let's exercise your cat!")
        # Dictionary of possible exercises
        EXERCISE = {"Chase a mouse": 0.4, "Climb a tree": 0.3, "Scratch a post": 0.2}
        print("")
        # Generating a menu of exercises for the user to pick from
        menu_generator_dict(EXERCISE, "EXERCISE MENU\nHere are the exercises your cat can do and how much weight it will lose if it does them: ")
        # Allowing user to select what exercise they want to do
        exercise_choice = integer_checker(3, 1, "Please enter either 1, 2, or 3", "Please enter either 1, 2, or 3", "Please enter the corresponding number to the exercise you would like your cat to do")
        # Providing feedback based on the exercise chosen by the user
        if exercise_choice == 1:
            print("Your cat has chased a mouse and has lost {}kg".format(EXERCISE["Chase a mouse"]))
            # Decreasing the cat's weight by the specific amount for the exercise
            weight = subtract(EXERCISE["Chase a mouse"], weight)
            # Checking if the cat's new weight is too low or near being too low
            weight = death_checker(weight, 3.5, 4.5, 0.3)
            # Ending the game if the cat has died
            if weight == "dead":
                break
            # Informing the user of their cat's new weight if it has not died
            else:
                print("{} now weighs {:.1f}kg".format(name, weight))
        elif exercise_choice == 2:
            print("Your cat has climbed a tree and has lost {}kg".format(EXERCISE["Climb a tree"]))
            # Decreasing the cat's weight by the specific amount for the exercise
            weight = subtract(EXERCISE["Climb a tree"], weight)
            # Checking if the cat's new weight is too low or near being too low
            weight = death_checker(weight, 3.5, 4.5, 0.3)
            # Ending the game if the cat has died
            if weight == "dead":
                break
            # Informing the user of their cat's new weight if it has not died
            else:
                print("{} now weighs {:.1f}kg".format(name, weight))
        elif exercise_choice == 3:
            print("Your cat has scratched a post and has lost {}kg".format(EXERCISE["Scratch a post"]))
            # Decreasing the cat's weight by the specific amount for the exercise
            weight = subtract(EXERCISE["Scratch a post"], weight)
            # Checking if the cat's new weight is too low or near being too low
            weight = death_checker(weight, 3.5, 4.5, 0.3)
            # Ending the game if the cat has died
            if weight == "dead":
                break
            # Informing the user of their cat's new weight if it has not died
            else:
                print("{} now weighs {:.1f}kg".format(name, weight))
    # Branch which runs if the user chooses to feed their cat
    elif activity_choice == 2:
        print("Let's feed your cat!")
        # Dictionary of possible foods
        FOODS = {"Salmon": 0.4, "Jelly meat": 0.3, "Biscuits": 0.2}
        print("")
        # Generating a food menu and their corresponding weight gain values
        menu_generator_dict(FOODS, "FOOD MENU\nHere are the foods your cat can eat and how much weight it will gain if it eats them: ")
        # Asking user to choose which food they want their cat to eat and checking that they have inputed an integer within the desired range
        food_choice = integer_checker(3, 1, "Please enter either 1, 2, or 3", "Please enter either 1, 2, or 3", "Please enter the corresponding number to the food you would like your cat to eat")
        # Providing feedback based on the food chosen by the user
        if food_choice == 1:
            print("Your cat has eaten salmon and has gained {}kg".format(FOODS["Salmon"]))
            # Increasing the cat's weight by the corresponding weight gain value to the chosen food
            weight = add(FOODS["Salmon"], weight)
            # Checking if the cat's new weight is too high or near being too high
            weight = death_checker(weight, 3.5, 4.5, 0.3)
            # Ending the game if the cat has died
            if weight == "dead":
                break
            # Informing the user of the cat's new weight if it has not died
            else:
                print("{} now weighs {:.1f}kg".format(name, weight))
        elif food_choice == 2:
            print("Your cat has eaten jelly meat and has gained {}kg".format(FOODS["Jelly meat"]))
            # Increasing the cat's weight by the corresponding weight gain value to the chosen food
            weight = add(FOODS["Jelly meat"], weight)
            # Checking if the cat's new weight is too high or near being too high
            weight = death_checker(weight, 3.5, 4.5, 0.3)
            # Ending the game if the cat has died
            if weight == "dead":
                break
            # Informing the user of the cat's new weight if it has not died
            else:
                print("{} now weighs {:.1f}kg".format(name, weight))
        elif food_choice == 3:
            print("Your cat has eaten biscuits and has gained {}kg".format(FOODS["Biscuits"]))
            # Increasing the cat's weight by the corresponding weight gain value to the chosen food
            weight = add(FOODS["Biscuits"], weight)
            # Checking if the cat's new weight is too high or near being too high
            weight = death_checker(weight, 3.5, 4.5, 0.3)
            # Ending the game if the cat has died)
            if weight == "dead":
                break
            # Informing the user of the cat's new weight if it has not died
            else:
                print("{} now weighs {:.1f}kg".format(name, weight))
    # Branch which runs if the user wants to check their cat's weight
    elif activity_choice == 3:
        print("Let's check your cat's weight!")
        # Telling the user their cat's weight
        print("{} weighs {}kg".format(name, weight))
        # Checking if the cat's weight is near being too low or high and telling the user if they need to feed or exercise their cat
        death_checker(weight, 3.5, 4.5, 0.3)
    # Branch which runs if the user wants to reread the instructions
    elif activity_choice == 4:
        # Printing the instructions
        print(""
              "The aim of this game is to keep your cat within a healthy weight range of 3.5 - 4.5kg. If you exercise your cat it will lose wight and if you feed your cat it will gain weight")
    # Ending the game if the user chooses to quit the game
    elif activity_choice == 5:
        generate = True

    # Reprinting the home menu after the user has done an activity which does not end the game and exit the loop
    menu_generator_list(home, "HOME MENU")

# Thanking the user for playing
print("Thank you for playing Virtual Cat Simulator!")
