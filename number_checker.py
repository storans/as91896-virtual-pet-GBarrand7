# Program to check if a pet's weight is within a certain range

# High and low are constants as they are not changed in this particular program

HIGH = 4.5
LOW = 3.5

# Keep going variable used to create loop for testing
keep_going = ""

# Loop to allow for continual testing of values
while keep_going == "":
    # Getting input from the user for their cat's weight
    weight = float(input("How much does your cat weigh?"))
    print("")
    # Weight is greater than or equal to 3.5 or less than or equal to 4.5 as these are still healthy weights
    if LOW <= weight <= HIGH:
        print("Your cat is in a healthy weight range")
        print("")
    elif weight < LOW:
        print("Your cat is underweight")
        print("")
    elif weight > HIGH:
        print("Your cat is overweight")
        print("")

    # Program asks for input in order to either continue or break the loop
    keep_going = input("If you would like to keep going press <enter>")
    print("")
