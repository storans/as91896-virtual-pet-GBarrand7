# Program to check if a pet's weight is within a certain range

# Function to check if a number is between two values
def number_checker(high, low, error_1, error_2, question):
    valid = False
    while valid == False:
        try:
            response = float(input("{} >> ".format(question)))
            if low <= response <= high:
                return response
            else:
                print(error_1)
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


