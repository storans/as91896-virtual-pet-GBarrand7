# Program to check if a pet's weight is within a certain range

# Function to check if a flaot is between two values
# Parameters:
# high - highest possible value
# low - lowest possible value
# error_1 - error for if the user has entered a float outside of the desired range
# error_2 - error for if the user has not entered a float
# question - question which asks for input
def number_checker(high, low, error_1, error_2, question):
    # Setting valid to false to run the loop
    valid = False
    # Loop runs until a valid input is entered
    while valid == False:
        # Checking if user has entered a valid float
        try:
            # Getting user's input in response to the question
            response = float(input("{} >> ".format(question)))
            # Checking if the user's response is within the desired range
            if low <= response <= high:
                # Returning response for use in the program
                return response
            # Branch which runs if user has entered a float outside of the range
            else:
                print(error_1)
        # Branch which runs if the user has not entered a float
        except ValueError:
            print(error_2)

# Keep going variable used to create loop for testing
keep_going = ""

# Loop to allow for continual testing of values
while keep_going == "":
    # Getting input from the user for their cat's weight
    weight = number_checker(4.5, 3.5, "Please enter a weight between 3.5kg - 4.5kg", "Please enter a number", "How much does your pet weigh?")
    print("You pet weighs {}kg".format(weight))
    print("")

    # Program asks for input in order to either continue or break the loop
    keep_going = input("If you would like to keep going press <enter>")
    print("")


