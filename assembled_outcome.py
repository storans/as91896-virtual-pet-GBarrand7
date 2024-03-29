# Georgia Barrand
# Assembled outcome - Version 8
# The purpose of this program is to provide a fun virtual cat simulator game for kids to play

# Import random module for use throughout the program
# to randomly generate various things - e.g names

import random

# List to store possible options on the numbered list
# of the name generator menu
NAME_CHOICE = ["Choose your own name", "Have a name randomly generated"]

# List of profanities which will be checked for
# In an actual outcome this list would need to be extended
PROFANITIES = ["anal", "anus", "arse", "ass", "asshole", "bastard",
               "bitch", "cock", "crap", "damn", "darn",
               "dick", "douche", "fuck", "fucker", "whore", "mother fuck",
               "mother fucker", "motherfucker", "penis", "piss", "porn",
               "retard", "sex", "sexy", "shit", "slut", "son of a bitch",
               "tits", "vagina"]

# Using a 2D list to store the names
# First list holds girls' names
# Second list holds boys' names
# Third list hold names which could be either gender
NAMES = [["Pixie", "Babushka", "Poppy", "Molly", "Tina", "Tinkerbell"],
         ["Lord Meowsworth", "Chad", "Ernie", "Clyde",
          "Mr Cat", "Garfield"],
         ["Mittens", "Fluffy", "Hairball", "Fleabag",
          "Minty", "Whiskers", "Ginger"]]

# 2D list of possible gender inputs
GENDERS = [['g', 'girl', 'f', 'female'],
           ['b', 'boy', 'male', 'm'],
           ['n', 'neutral', 'gn', 'gender neutral']]

# List of wanted values for the home menu in the numbered list
HOME = ["Exercise your cat", "Feed your cat", "Check your cat's weight",
        "See the game instructions", "Quit"]

# Dictionary of possible exercises
EXERCISE = {"Chase a mouse": 0.4, "Climb a tree": 0.3, "Scratch a post": 0.2}

# Dictionary of possible foods
FOODS = {"Salmon": 0.4, "Jelly meat": 0.3, "Biscuits": 0.2}

# Messages for if the cat has died from being too overweight
# or too underweight, or if they are near being
# too underweight or overweight
TOO_HIGH = "Unfortunately, your cat has eaten too much and has passed away.\
 Make sure to exercise your cat more next time."

TOO_LOW = "Unfortunately, your cat has not eaten enough and has passed away.\
 Make sure to feed your cat more next time."

NEAR_LOW = "Make sure to feed your cat soon!"

NEAR_HIGH = "Make sure to exercise your cat soon!"


# Function to randomly generate a name
# Parameters:
# list_segment - what part of the 2D list the name is generated from
# based on the desired gender
# list_name - the list the names are stored in
# message - asking the user if they like the name or not
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
        # Loop runs while not valid
        while not valid:
            # Asking if the user likes the name generated
            # Making the input lowercase
            # Removing any spaces before or after
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
                # Setting valid to true to break the loop
                # instead of repeatedly asking if the user likes the name
                valid = True
            # Branch that runs if the user enters an invalid input for generate
            else:
                print("Please enter either yes or no")
    # Returning the selected randomly generated name
    return name


# Function to convert user's gender input to the desired input
# if their input is within an approved list
# Parameters:
# question - the question asked
# error - the error message if the user enters none of the desired inputs
def input_converter(question, error):
    # Setting valid to False
    valid = False
    # Function asks for input until the user inputs a valid response
    while not valid:
        # Asking user what gender name they would like
        # Making the input lowercase
        # Removing any spaces before or after
        gender = input("{} >> ".format(question)).strip().lower()
        # Checking if the gender is within the
        # approved list of inputs for female gender
        if gender in GENDERS[0]:
            # Changing input to the standard input
            gender = "g"
            return gender
        # Checking if the gender is within the
        # approved list of inputs for male gender
        elif gender in GENDERS[1]:
            # Changing input to the standard input
            gender = "b"
            return gender
        # Checking if the gender is within the
        # approved list of inputs for gender neutral
        elif gender in GENDERS[2]:
            # Changing input to the standard input
            gender = "n"
            return gender
        # Branch which runs if the user does not enter
        # any valid input for gender
        else:
            print(error)


# Functions to increase or decrease the cat's weight

# Parameters:
# amount - the amount of weight to be added or subtracted
# weight - the weight of the cat
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
# Parameters
# new_weight - the cat's weight after being fed or exercised
# low - the lowest possible weight the cat can be
# high - the highest possible weight the cat can be
# boundary - the bracket within which the cat is near being
# overweight or underweight
def death_checker(new_weight, low, high, boundary):
    # If cat's weight is below the lowest weight
    if new_weight < low:
        print(TOO_LOW)
        # Setting cat's weight to "dead"
        #  and returning this for use in the program
        new_weight = "dead"
        return new_weight
    # If cat's weight is above the highest weight
    elif new_weight > high:
        print(TOO_HIGH)
        # Setting cat's weight to "dead"
        # and returning this for use in the program
        new_weight = "dead"
        return new_weight
    # If cat's weight is between the lowest weight
    # and a weight near the lowest weight (e.g 3.5 - 3.8)
    elif low <= new_weight <= (low + boundary):
        print(NEAR_LOW)
        return new_weight
    # If cat's weight is below the highest weight
    # and a weight near the highest weight (e.g 4.2 - 4.5
    elif high >= new_weight >= (high - boundary):
        print(NEAR_HIGH)
        return new_weight
    # If the cat is in a healthy weight range
    else:
        return new_weight


# Functions to generate a menu

# Menu generator for list stored data
# Parameters:
# list - the list the data is stored in
# starting_message - the message wanted before the numbered list
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
# Parameters:
# dictionary - the dictionary name where the data is stored
# starting_message - the message wanted before the numbered list
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
# Parameters:
# high - the highest possible value
# low - the lowest possible value
# error_1 - the error for if the user has entered a number outside of the range
# error_2 - the error for if the user hasn't entered a number
# question - the question being asked of the user
def float_checker(high, low, error_1, error_2, question):
    # Setting valid to false to run the loop
    valid = False
    # Loop runs while valid is false so the question is asked
    # until a valid answer is entered
    while not valid:
        try:
            # Getting the user's response
            response = float(input("{} >> ".format(question)))
            # If the response entered is a number within the designated range
            # then the response is returned
            if low <= response <= high:
                return response
            # If the response is outside of the range
            # then the first error message is displayed
            else:
                print(error_1)
        # If the user does not enter a number
        # then the second error is displayed
        except ValueError:
            print(error_2)


# Function to check if a integer is between two values
# Parameters:
# high - the highest possible value
# low - the lowest possible value
# error_1 - the error for if the user has entered a number outside of the range
# error_2 - the error for if the user hasn't entered a number
# question - the question being asked of the user
def integer_checker(high, low, error_1, error_2, question):
    # Setting valid to false to run the loop
    valid = False
    # Loop runs while valid is false so the question is asked
    # until a valid answer is entered
    while not valid:
        try:
            # Getting the user's response
            response = int(input("{} >> ".format(question)))
            # If the user has entered an integer within the range
            # then the response is returned
            if low <= response <= high:
                return response
            # If the user has entered an integer outside of the range
            # then the first error is displayed
            else:
                print(error_1)
        # If the user has not entered an integer
        # then the second error is displayed
        except ValueError:
            print(error_2)


# Function to check if the name the user has entered is appropriate
# or not in terms of profanity
# Parameter: message - question to get the name input from the user
def profanity_checker(message):

    # Setting valid to false to run the loop
    valid = False
    # User is asked for input until a valid answer is inputted
    # as the loop will continue to run
    while not valid:
        # Asking the user for input of the name
        # Making it lowercase
        # Removing any spaces before or after the input
        name = input(message).lower().strip()
        # Checking if the name is in the list of profanities
        if name in PROFANITIES:
            # Error message saying that the name entered is not appropriate
            print("That is not a nice name. Please enter a different name")
        # Checking if the user has not entered a name
        elif name == "":
            # Error message for if the user has not entered a name
            print("Please enter a name")
        # Branch which runs if the user has entered an appropriate name
        else:
            # Making the starting letter of the name capitalised
            name = name.title()
            print("{} is a wonderful name!".format(name))
            # Returning the name for use in the program
            return name


if __name__ == "__main__":
    # Start of game

    print("Hello, and welcome to the Virtual Cat Simulator!\n"
          "In this game you can name your cat, feed it and exercise it.\n"
          "But, be careful! If your cat gets is not fed enough or is not \
exercised enough it can pass away,\n"
          "so make sure your cat stays in a \
healthy weight range of 3.5-4.5kg.\n"
          "We hope you enjoy the game!")

    print("")

    # Generating a menu to show the user the options
    # they have for selecting a name
    menu_generator_list(NAME_CHOICE,
                        "First, let's name your cat. You have two options: ")

    # Allowing user to make their choice for how to name their pet
    choice = integer_checker(2, 1, "Please enter either 1 or 2",
                             "Please enter either 1 or 2",
                             "Enter either 1 or 2 to select \
how you want to name your cat")
    # If user chooses to enter their own name
    if choice == 1:

        # Allowing the user to enter a name
        # and checking it is appropriate using the profanity checker
        name = profanity_checker("What would you like to name your cat? ")

    # If user chooses to have a name generated for them
    elif choice == 2:

        # Allowing user to choose what gender name they would like
        gender = input_converter("Would you like a girl's name or a boy's name? \
Enter <g> for girl, <b> for boy or <n> for a gender neutral name",
                                 "Please enter either <g>, <b> or <n>")
        # If user chooses that they want a girl's name
        if gender == "g":
            # Randomly generating a name from the girl's name list
            # until the user says they like the name
            # using the name_generator function
            name = name_generator(0, NAMES, "Do you like this name? \
Enter 'yes' to choose this name or 'no' to generate another name >> ")
            print("Your cat's name is {}".format(name))
        # If user chooses that they want a boy's name
        elif gender == "b":
            # Randomly generating a name from the boy's name list
            # until the user says they like the name
            # using the name_generator function
            name = name_generator(1, NAMES, "Do you like this name? \
Enter 'yes' to choose this name or 'no' to generate another name >> ")
            print("Your cat's name is {}".format(name))
        # If user chooses that they want a gender neutral name
        elif gender == "n":
            # Randomly generating a name from the gender neutral name list
            # until the user says they like the name
            # using the name_generator function
            name = name_generator(2, NAMES, "Do you like this name? \
Enter 'yes' to choose this name or 'no' to generate another name >> ")
            print("Your cat's name is {}".format(name))

    print("")
    print("Now, you can choose {}'s starting weight.".format(name))
    # Allowing user to choose their cat's starting weight
    weight = float_checker(4.5, 3.5, "Please enter a weight between 3.5kg - 4.5kg",
                           "Please enter a number",
                           "Please pick a weight between 3.5 - 4.5kg")
    # Informing user of their cat's weight
    # and reminding them of the rules and then showing them a cat graphic
    print("{} weighs {:.1f}kg. Make sure to keep {} \
within a healthy weight range of 3.5 - 4.5kg".format(name, weight, name))
    print("")
    print("Here is your cat {}!\n      \    /\\"
          "\n       )  ( ')\n      (  /  )\n       \(__)|".format(name))

    # Home Menu
    print("")
    print("You are now set up to play Virtual Cat Simulator! \
We hope you enjoy the game!")

    # Setting the number of turns taken to 0 at the start of the game
    turns = 0

    # Loop runs while generate is equal to false
    while turns <= 20:
        # Generating the home menu
        print("")
        menu_generator_list(HOME, "HOME MENU")
        print("")

        # Getting user's choice of activity from the menu
        # and checking that it is within the wanted range
        activity_choice = integer_checker(5, 1,
                                          "Please enter a number between 1-5",
                                          "Please enter a number between 1-5",
                                          "What would you like to do? \
Select the corresponding number from the menu above")
        # User chooses to exercise their cat
        if activity_choice == 1:
            print("Let's exercise your cat!")
            print("")
            # Generating a menu of exercises for the user to pick from
            menu_generator_dict(EXERCISE, "EXERCISE MENU\n"
                                          "Here are the exercises your cat can do and \
how much weight it will lose if it does them: ")
            # Adding option to go back to home menu
            # separately as it uses different formatting
            print("4. Go back to the home menu")
            # Allowing user to select what exercise
            # they want to do or to go back to the home menu
            print("")
            exercise_choice = integer_checker(4, 1,
                                              "Please enter either 1, 2, 3 or 4",
                                              "Please enter either 1, 2, 3 or 4",
                                              "Please enter the corresponding number \
to the exercise you would like your cat to do")
            print("")
            # Providing feedback based on the exercise chosen by the user
            if exercise_choice == 1:
                print("Your cat has chased a mouse and has lost {}kg"
                      .format(EXERCISE["Chase a mouse"]))
                # Decreasing the cat's weight
                # by the specific amount for the exercise
                weight = subtract(EXERCISE["Chase a mouse"], weight)
                # Checking if the cat's new weight is too low or near being too low
                weight = death_checker(weight, 3.5, 4.5, 0.3)
                # Ending the game if the cat has died
                if weight == "dead":
                    break
                # Informing the user of their cat's new weight if it has not died
                else:
                    print("{} now weighs {:.1f}kg".format(name, weight))
                    # Increasing the number of turns taken by 1
                    turns += 1

            elif exercise_choice == 2:
                print("Your cat has climbed a tree and has lost {}kg"
                      .format(EXERCISE["Climb a tree"]))
                # Decreasing the cat's weight
                # by the specific amount for the exercise
                weight = subtract(EXERCISE["Climb a tree"], weight)
                # Checking if the cat's new weight is too low or near being too low
                weight = death_checker(weight, 3.5, 4.5, 0.3)
                # Ending the game if the cat has died
                if weight == "dead":
                    break
                # Informing the user of their cat's new weight if it has not died
                else:
                    print("{} now weighs {:.1f}kg".format(name, weight))
                    # Increasing the number of turns taken by 1
                    turns += 1

            elif exercise_choice == 3:
                print("Your cat has scratched a post and has lost {}kg"
                      .format(EXERCISE["Scratch a post"]))
                # Decreasing the cat's weight
                # by the specific amount for the exercise
                weight = subtract(EXERCISE["Scratch a post"], weight)
                # Checking if the cat's new weight is too low or near being too low
                weight = death_checker(weight, 3.5, 4.5, 0.3)
                # Ending the game if the cat has died
                if weight == "dead":
                    break
                # Informing the user of their cat's new weight if it has not died
                else:
                    print("{} now weighs {:.1f}kg".format(name, weight))
                    # Increasing the number of turns taken by 1
                    turns += 1

            # Branch which runs if the user wants to go back to the home menu
            elif exercise_choice == 4:
                print("")
        # Branch which runs if the user chooses to feed their cat
        elif activity_choice == 2:
            print("Let's feed your cat!")
            print("")
            # Generating a food menu and their corresponding weight gain values
            menu_generator_dict(FOODS,
                                "FOOD MENU\nHere are the foods your cat can eat \
and how much weight it will gain if it eats them: ")
            # Printing option to go back to the home menu
            # separately as it uses different formatting
            print("4. Go back to the home menu")
            # Asking user to choose which food they want their cat to eat
            # and checking that they have inputted an integer
            # within the desired range
            print("")
            food_choice = integer_checker(4, 1,
                                          "Please enter either 1, 2, 3 or 4",
                                          "Please enter either 1, 2, 3 or 4",
                                          "Please enter the corresponding number \
to the food you would like your cat to eat")
            print("")
            # Providing feedback based on the food chosen by the user
            if food_choice == 1:
                print("Your cat has eaten salmon and has gained {}kg"
                      .format(FOODS["Salmon"]))
                # Increasing the cat's weight
                # by the corresponding weight gain value to the chosen food
                weight = add(FOODS["Salmon"], weight)
                # Checking if the cat's new weight
                # is too high or near being too high
                weight = death_checker(weight, 3.5, 4.5, 0.3)
                # Ending the game if the cat has died
                if weight == "dead":
                    break
                # Informing the user of the cat's new weight if it has not died
                else:
                    print("{} now weighs {:.1f}kg".format(name, weight))
                    # Increasing the number of turns taken by 1
                    turns += 1

            elif food_choice == 2:
                print("Your cat has eaten jelly meat and has gained {}kg"
                      .format(FOODS["Jelly meat"]))
                # Increasing the cat's weight
                # by the corresponding weight gain value to the chosen food
                weight = add(FOODS["Jelly meat"], weight)
                # Checking if the cat's new weight
                # is too high or near being too high
                weight = death_checker(weight, 3.5, 4.5, 0.3)
                # Ending the game if the cat has died
                if weight == "dead":
                    break
                # Informing the user of the cat's new weight if it has not died
                else:
                    print("{} now weighs {:.1f}kg".format(name, weight))
                    # Increasing the number of turns taken by 1
                    turns += 1

            elif food_choice == 3:
                print("Your cat has eaten biscuits and has gained {}kg"
                      .format(FOODS["Biscuits"]))
                # Increasing the cat's weight
                # by the corresponding weight gain value to the chosen food
                weight = add(FOODS["Biscuits"], weight)
                # Checking if the cat's new weight
                # is too high or near being too high
                weight = death_checker(weight, 3.5, 4.5, 0.3)
                # Ending the game if the cat has died)
                if weight == "dead":
                    break
                # Informing the user of the cat's new weight if it has not died
                else:
                    print("{} now weighs {:.1f}kg".format(name, weight))
                    # Increasing the number of turns taken by 1
                    turns += 1

            # Branch which runs if user wants to return to the home menu
            elif food_choice == 4:
                print("")
        # Branch which runs if the user wants to check their cat's weight
        elif activity_choice == 3:
            print("")
            print("Let's check your cat's weight!")
            # Telling the user their cat's weight
            print("{} weighs {:.1f}kg".format(name, weight))
            # Checking if the cat's weight is near being too low or high
            # and telling the user if they need to feed or exercise their cat
            death_checker(weight, 3.5, 4.5, 0.3)
        # Branch which runs if the user wants to reread the instructions
        elif activity_choice == 4:
            print("")
            # Printing the instructions
            print(""
                  "The aim of this game is to keep your cat \
within a healthy weight range of 3.5 - 4.5kg.\n"
                  "If you exercise your cat it will lose weight \
and if you feed your cat it will gain weight")
        # Ending the game if the user chooses to quit the game
        elif activity_choice == 5:
            break

    # Message for if the user has not killed their cat but has had the maximum number of turns
    if turns == 21:
        print("")
        print("You have taken excellent care of {} and have won the game!".format(name))

    # Thanking the user for playing
    print("")
    print("Thank you for playing Virtual Cat Simulator!")
