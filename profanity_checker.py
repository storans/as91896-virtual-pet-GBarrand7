# Function to check if the name the user has entered is appropriate or not int terms of profanity
# Parameter: message - question to get the name input from the user
def profanity_checker(message):
    # List of profanities which will be checked for
    profanities = ["anal", "anus", "arse", "ass", "asshole", "bastard", "bitch", "cock", "crap", "cunt", "damn", "darn",\
                   "dick", "douche", "fuck", "fucker", "whore", "mother fuck", "mother fucker", "motherfucker", "penis", "piss",\
                    "porn", "retard", "sex", "sexy", "shit", "slut", "son of a bitch", "tits", "vagina"]
    # Setting valid to false to run the loop
    valid = False
    # User is asked for input until a valid answer is inputted as the loop will continue to run
    while valid == False:
        # Asking the user for input of the name, making it lowercase and removing any spaces before or after the input
        name = input(message).lower().strip()
        # Checking if the name is in the list of profanities
        if name in profanities:
            # Error message saying that the name entered is not appropriate
            print("That is not a nice name. Please enter a different name")
        # Branch which runs if the user has entered an appropriate name
        else:
            # Making the starting letter of the name capitalised
            name = name.title()
            print("{} is a wonderful name!".format(name))
            # Returning the name for use in the program
            return name

name = profanity_checker("What would you like to name your cat? ")

