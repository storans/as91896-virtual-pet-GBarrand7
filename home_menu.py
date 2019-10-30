# Home menu and start of the game

# Game welcome message
print("Hello, and welcome to the virtual cat simulator!\n"
      "In this game you can name your cat, feed it and exercise it.\nBut, be careful!\nIf your cat gets too skinny or too fat it can die, so make sure your cat stays in a healthy weight range of 3.5-4.5kg.\nWe hope you enjoy the game!")

# The users options of activities to do
print("1. Exercise your cat")
print("2. Feed your cat")
print("3. Check your cat's weight")
print("4. See the game instructions")
print("5. Quit")

# Variable to allow for continuous loop testing
keep_going = ""
# Setting valid to false to run the loop which asks for input until the user enters a valid input
valid = False
# Loop for testing purposes
while keep_going == "":
    # Asking for input until user enters a valid input
      while valid == False:
          # Getting user's choice of activity from the menu
          # Trialling using storing the input as a string at this stage for the numbers in order to make any other inputs invalid including strings however will use integer checking function in assembled outcome
            activity_choice = input("What would you like to do? Select the corresponding number from the menu above >>")
            # Providing feedback based on the user's choice of activity from the menu
            if activity_choice == "1":
                  print("Let's exercise your cat!")
                  # Breaking the loop as user has entered a valid input
                  valid = True
            elif activity_choice == "2":
                  print("Let's feed your cat!")
                  # Breaking the loop as user has entered a valid input
                  valid = True
            elif activity_choice == "3":
                  print("Let's check your cat's weight!")
                  # Breaking the loop as user has entered a valid input
                  valid = True
            elif activity_choice == "4":
                  print("Here are the instructions...")
                  # Breaking the loop as user has entered a valid input
                  valid = True
            elif activity_choice == "5":
                  print("Thanks for playing!")
                  # Breaking the loop as user has entered a valid input
                  valid = True
            # Branch which runs if the user does not enter a valid input which then loops back to ask the user for input again
            else:
                  print("Please enter either 1, 2, 3, 4 or 5")
    # Checking if the loop is needed to keep going for testing
      keep_going = input("Press <enter> to continue")
    # Resetting valid to False due to continual testing
      valid = False
