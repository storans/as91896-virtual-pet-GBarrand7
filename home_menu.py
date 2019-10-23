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
valid = False
# Loop for testing purposes
while keep_going == "":
    # Asking for input until user enters a valid input
      while valid == False:
          # Getting user's choice of activity from the menu
            activity_choice = input("What would you like to do? Select the corresponding number from the menu above >>")
            if activity_choice == "1":
                  print("Let's exercise your cat!")
                  valid = True
            elif activity_choice == "2":
                  print("Let's feed your cat!")
                  valid = True
            elif activity_choice == "3":
                  print("Let's check your cat's weight!")
                  valid = True
            elif activity_choice == "4":
                  print("Here are the instructions...")
                  valid = True
            elif activity_choice == "5":
                  print("Thanks for playing!")
                  valid = True
            else:
                  print("Please enter either 1, 2, 3, 4 or 5")
    # Checking if the loop is needed to keep going for testing
      keep_going = input("Press <enter> to continue")
    # Resetting valid to False due to continual testing
      valid = False
