# Program to check is person if eligible for superannuation
# Superannuation age is a constant as it is not changed in the program
SUPER_AGE = 65
keep_going = ""

# Loop to allow for continual testing of different values
while keep_going == "":
    age = int(input("How old are you?"))
    # Must be greater than or equal to as 65 year olds are eligible for superannuation
    if age >= SUPER_AGE:
        print("Yes super")
    else:
        print("NO SUPER FOR YOU!!")

    # Asks user for input to either break or continue the loop
    keep_going = input("If you want to continue press <enter> otherwise press any other letter to quit")

print("Thanks for telling us your personal details we will now sell them ;)")
