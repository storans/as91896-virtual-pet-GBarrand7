# Program to convert user input to the expected value when they enter a gender
keep_going = ""
# Setting valid variable to false so that the loop runs
valid = False
# Loop for testing
while keep_going == "":
    # Program keeps asking for input until user gives a valid input
    while valid == False:
        # Asking user what gender name they would like
        gender = input("Would you like a girl's name or a boy's name? Press <g> for girl, <b> for boy or <n> for a gender neutral name >>")
        # Allow user to enter multiple expected inputs to select a girl's name
        if gender == "female" or gender == "f" or gender == "girl" or gender == "g":
            gender = "g"
            print(gender)
            valid = True
        # Allow user to enter multiple expected inputs to select a boy's name
        elif gender == "male" or gender == "m" or gender == "boy" or gender == "b":
            gender = "b"
            print(gender)
            valid = True
        # Allow user to enter multiple expected inputs to select a gender neutral name
        elif gender == "gender neutral" or gender == "g n" or gender == "neutral" or gender == "n":
            gender = "n"
            print(gender)
            valid = True
        else:
            print("Please enter either <g>, <b> or <n> to select what gender name you would like")
    keep_going = input("Would you like to keep going? Press <enter> to continue")
    valid = False
